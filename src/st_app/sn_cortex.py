import sys
from pathlib import Path
file = Path(__file__).resolve() #cwd = Path.cwd()
parent, root_path = file.parent, file.parents[1]
sys.path.append(str(root_path)+"/")
print(sys.path)

from utils.utils_logger import setup_logger
logger = setup_logger(module_name=str(__name__))


import configparser
relative_path_1 = "/config/"
config_file_dir = str(file.parents[1]) + relative_path_1

config = configparser.ConfigParser()
config.read(str(config_file_dir)+"proj_cortex_.ini")
PASSWORD= config.get("SNOWFLAKE_CONNECTOR","PASSWORD")
ROLE= config.get("SNOWFLAKE_CONNECTOR","ROLE")
USER= config.get("SNOWFLAKE_CONNECTOR","USER")
CORTEX_ACCOUNT = config.get("SNOWFLAKE_CONNECTOR","ACCOUNT")
HOST = config.get("SNOWFLAKE_CONNECTOR","HOST")

DATABASE = "CORTEX_ANALYST_DEMO"
SCHEMA = "REVENUE_TIMESERIES"
STAGE = "RAW_DATA"
FILE = "revenue_timeseries.yaml"
WAREHOUSE = "cortex_analyst_wh"

from typing import Any, Dict, List, Optional
import pandas as pd
import requests
import snowflake.connector
import streamlit as st


class SnowCortex:
    """
    """
    
    @classmethod
    def get_conn(self):
        """
        Desc:
            - get CORTEX_ACCOUNT Connection 
        """
        try:
            if 'CONN' not in st.session_state or st.session_state.CONN is None:
                st.session_state.CONN = snowflake.connector.connect(
                                    user=USER,
                                    password=PASSWORD,
                                    account=CORTEX_ACCOUNT,
                                    # host=HOST,
                                    # port=443, ##80
                                    #authenticator="externalbrowser", ## Hangs 
                                    warehouse=WAREHOUSE,
                                    role=ROLE,
                                    enable_connection_diag=True,) #enable_connection_diag=True,--> verbose ERROR Logs 

                logger.debug(f"-init-st.session_state.CONN-->> {st.session_state.CONN}")
                return st.session_state.CONN
            
        except Exception as err:
            logger.error(f"--Error--get_conn->> {err}")



def send_message(prompt: str) -> Dict[str, Any]:
    """Calls the REST API and returns the response."""
    request_body = {
                        "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
                        "semantic_model_file": f"@{DATABASE}.{SCHEMA}.{STAGE}/{FILE}",
                    }
    
    st.session_state.CONN = SnowCortex().get_conn()
    resp = requests.post(
        url=f"https://{HOST}/api/v2/cortex/analyst/message",
        json=request_body,
        headers={
            "Authorization": f'Snowflake Token="{st.session_state.CONN.rest.token}"',
            "Content-Type": "application/json",
        },
    )
    request_id = resp.headers.get("X-Snowflake-Request-Id")
    if resp.status_code < 400:
        return {**resp.json(), "request_id": request_id}  # type: ignore[arg-type]
    else:
        raise Exception(
                        f"Failed request (id: {request_id}) with status {resp.status_code}: {resp.text}"
                    )

# user_prompt = "hello whats the count of cars"
# send_message(prompt=user_prompt)


def process_message(prompt: str) -> None:
    """Processes a message and adds the response to the chat."""
    st.session_state.messages.append(
        {"role": "user", "content": [{"type": "text", "text": prompt}]}
    )
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = send_message(prompt=prompt)
            request_id = response["request_id"]
            content = response["message"]["content"]
            display_content(content=content, request_id=request_id)  # type: ignore[arg-type]
    st.session_state.messages.append(
        {"role": "assistant", "content": content, "request_id": request_id}
    )

def display_content(
                    content: List[Dict[str, str]],
                    request_id: Optional[str] = None,
                    message_index: Optional[int] = None,
                ) -> None:
    """Displays a content item for a message."""
    message_index = message_index or len(st.session_state.messages)
    if request_id:
        with st.expander("Request ID", expanded=False):
            st.markdown(request_id)
    for item in content:
        if item["type"] == "text":
            st.markdown(item["text"])
        elif item["type"] == "suggestions":
            with st.expander("Suggestions", expanded=True):
                for suggestion_index, suggestion in enumerate(item["suggestions"]):
                    if st.button(suggestion, key=f"{message_index}_{suggestion_index}"):
                        st.session_state.active_suggestion = suggestion
        elif item["type"] == "sql":
            
            st.session_state.CONN = SnowCortex().get_conn()

            with st.expander("SQL Query", expanded=False):
                st.code(item["statement"], language="sql")
            with st.expander("Results", expanded=True):
                with st.spinner("Running SQL..."):
                    df = pd.read_sql(item["statement"], st.session_state.CONN)
                    if len(df.index) > 1:
                        data_tab, line_tab, bar_tab = st.tabs(
                            ["Data", "Line Chart", "Bar Chart"]
                        )
                        data_tab.dataframe(df)
                        if len(df.columns) > 1:
                            df = df.set_index(df.columns[0])
                        with line_tab:
                            st.line_chart(df)
                        with bar_tab:
                            st.bar_chart(df)
                    else:
                        st.dataframe(df)

st.title("Cortex Analyst")
st.markdown(f"Semantic Model: {FILE}")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.suggestions = []
    st.session_state.active_suggestion = None

for message_index, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        display_content(
            content=message["content"],
            request_id=message.get("request_id"),
            message_index=message_index,
        )

if user_input := st.chat_input("What is your question?"):
    process_message(prompt=user_input)

if st.session_state.active_suggestion:
    process_message(prompt=st.session_state.active_suggestion)
    st.session_state.active_suggestion = None

