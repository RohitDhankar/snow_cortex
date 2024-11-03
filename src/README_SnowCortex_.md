
## SnowFlake - Cortex Analyst- Intro Tutorials -
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/tutorials/tutorial-1#step-1-setup

- TODO -[semantic-model-spec](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec)

- TODO - [ENABLE_CORTEX_ANALYST_MODEL_AZURE_OPENAI](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst#enable-cortex-analyst-model-azure-openai)

- TODO - [Streamlit_in_SnowflakeApp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst#label-copilot-create-streamlit-app)
- Streamlit in Snowflake (SiS)
- 


- TODO - [DBT-dbt Quickstarts](https://docs.getdbt.com/docs/introduction)
- TODO - [DBT-dbt Quickstarts](https://docs.getdbt.com/docs/get-started-dbt)

- https://docs.snowflake.com/en/developer-guide/snowflake-python-api/tutorials/common-setup 

<br/>

#### Cortex Analyst - Pre Intro Steps for SetUp
- [snowflake-in-20minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes)

- Create Snowflake objects—You create a database and a table for storing data.
- Install SnowSQL—You install and use SnowSQL, the Snowflake command line query tool.
Users of Visual Studio Code might consider using the Snowflake Extension for Visual Studio Code instead of SnowSQL.
- Load CSV data files—You use various mechanisms to load data into tables from CSV files.
- Write and execute sample queries—You write and execute a variety of queries against newly loaded data.


#### Cortex Analyst - Intro 

- ```Cortex Analyst``` - transforms natural-language questions about your data into results by generating and executing SQL queries. 
- This tutorial describes how to set up Cortex Analyst to respond to questions about a time-series revenue data set. 

- [Cortex Analyst-Tutorial](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/tutorials/tutorial-1#introduction)

<br/>

#### Cortex Analyst - Streamlit App 
- Step 3: Create a Streamlit app to talk to your data through Cortex Analyst
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/tutorials/tutorial-1#step-3-create-a-streamlit-app-to-talk-to-your-data-through-cortex-analyst

<br/>

#### SnowSQL - Snowflake CLI (CLI client)

- ```Snowflake CLI``` - is an open-source command-line tool explicitly designed for developer-centric workloads in addition to SQL operations. As an alternative to SnowSQL, Snowflake CLI lets you execute SQL commands as well as execute commands for other Snowflake products like Streamlit in Snowflake, Snowpark Container Services, and Snowflake Native App Framework. Snowflake recommends that you begin transitioning from SnowSQL to Snowflake CLI.

- LINUX Install --  download, verify, and run the installer package to install SnowSQL on Linux.
- [SnowSQL-LINUX Install](https://docs.snowflake.com/en/user-guide/snowsql-install-config#installing-snowsql-on-linux-using-the-installer)
- get the RPM package from here -- https://developers.snowflake.com/snowsql/
- ```SNOWSQL_DOWNLOAD_DIR``` -- In addition, you can separate the download directory from the configuration file by setting the SNOWSQL_DOWNLOAD_DIR environment variable so that multiple SnowSQL processes can share the binaries.

<br/>

#### Snowflake API Reference (Python)
- https://docs.snowflake.com/developer-guide/snowflake-python-api/reference/latest/index
- The Snowflake platform has a rich SQL command API which lets you interact with Snowflake entities, creating, deleting, modifying them, and more. The library described here, called the “Snowflake Python API” (or “SnowAPI” for short) provides the same functionality using the Python language.

<br/>

#### Snowflake Connector for Python
- https://docs.snowflake.com/developer-guide/python-connector/python-connector
- 
- snowflake.core



<br/>

##### RPM install not recommended -- use the .bash -- for SnowSQL CLI 
- ```bash snowsql-1.3.2-linux_x86_64.bash```
-  

```shell
(base) dhankar@dhankar-1:~/.../config$ ls -lahtr
total 27M
-rw-rw-r-- 1 dhankar dhankar  230 Nov  3 13:39 proj_cortex_.ini
drwxrwxr-x 5 dhankar dhankar 4.0K Nov  3 13:46 ..
-rw-rw-r-- 1 dhankar dhankar  27M Nov  3 14:18 snowflake-snowsql-1.3.1-1.x86_64.rpm
drwxrwxr-x 2 dhankar dhankar 4.0K Nov  3 14:23 .
(base) dhankar@dhankar-1:~/.../config$ 
(base) dhankar@dhankar-1:~/.../config$ rpm -i snowflake-snowsql-1.3.1-1.x86_64.rpm

Command 'rpm' not found, but can be installed with:

sudo apt install rpm

(base) dhankar@dhankar-1:~/.../config$ sudo apt install rpm
[sudo] password for dhankar: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  debugedit librpm8 librpmbuild8 librpmio8 librpmsign8 rpm-common rpm2cpio
Suggested packages:
  rpm-i18n alien elfutils rpmlint rpm2html
The following NEW packages will be installed:
  debugedit librpm8 librpmbuild8 librpmio8 librpmsign8 rpm rpm-common rpm2cpio
0 upgraded, 8 newly installed, 0 to remove and 232 not upgraded.
Need to get 501 kB of archives.
After this operation, 1,989 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 librpmio8 amd64 4.14.1+dfsg1-2 [74.6 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 debugedit amd64 4.14.1+dfsg1-2 [19.1 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 librpm8 amd64 4.14.1+dfsg1-2 [173 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 librpmbuild8 amd64 4.14.1+dfsg1-2 [70.5 kB]
Get:5 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 librpmsign8 amd64 4.14.1+dfsg1-2 [8,184 B]
Get:6 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 rpm-common amd64 4.14.1+dfsg1-2 [28.7 kB]
Get:7 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 rpm2cpio amd64 4.14.1+dfsg1-2 [7,988 B]
Get:8 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 rpm amd64 4.14.1+dfsg1-2 [119 kB]
Fetched 501 kB in 1s (384 kB/s)
Selecting previously unselected package librpmio8.
(Reading database ... 355334 files and directories currently installed.)
Preparing to unpack .../0-librpmio8_4.14.1+dfsg1-2_amd64.deb ...
Unpacking librpmio8 (4.14.1+dfsg1-2) ...
Selecting previously unselected package debugedit.
Preparing to unpack .../1-debugedit_4.14.1+dfsg1-2_amd64.deb ...
Unpacking debugedit (4.14.1+dfsg1-2) ...
Selecting previously unselected package librpm8.
Preparing to unpack .../2-librpm8_4.14.1+dfsg1-2_amd64.deb ...
Unpacking librpm8 (4.14.1+dfsg1-2) ...
Selecting previously unselected package librpmbuild8.
Preparing to unpack .../3-librpmbuild8_4.14.1+dfsg1-2_amd64.deb ...
Unpacking librpmbuild8 (4.14.1+dfsg1-2) ...
Selecting previously unselected package librpmsign8.
Preparing to unpack .../4-librpmsign8_4.14.1+dfsg1-2_amd64.deb ...
Unpacking librpmsign8 (4.14.1+dfsg1-2) ...
Selecting previously unselected package rpm-common.
Preparing to unpack .../5-rpm-common_4.14.1+dfsg1-2_amd64.deb ...
Unpacking rpm-common (4.14.1+dfsg1-2) ...
Selecting previously unselected package rpm2cpio.
Preparing to unpack .../6-rpm2cpio_4.14.1+dfsg1-2_amd64.deb ...
Unpacking rpm2cpio (4.14.1+dfsg1-2) ...
Selecting previously unselected package rpm.
Preparing to unpack .../7-rpm_4.14.1+dfsg1-2_amd64.deb ...
Unpacking rpm (4.14.1+dfsg1-2) ...
Setting up librpmio8 (4.14.1+dfsg1-2) ...
Setting up debugedit (4.14.1+dfsg1-2) ...
Setting up librpm8 (4.14.1+dfsg1-2) ...
Setting up rpm-common (4.14.1+dfsg1-2) ...
Setting up librpmsign8 (4.14.1+dfsg1-2) ...
Setting up librpmbuild8 (4.14.1+dfsg1-2) ...
Setting up rpm2cpio (4.14.1+dfsg1-2) ...
Setting up rpm (4.14.1+dfsg1-2) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.5) ...
(base) dhankar@dhankar-1:~/.../config$ 
(base) dhankar@dhankar-1:~/.../config$ rpm -i snowflake-snowsql-1.3.1-1.x86_64.rpm
rpm: RPM should not be used directly install RPM packages, use Alien instead!
rpm: However assuming you know what you are doing...
error: unpacking of archive failed: cpio: mkdir failed - Permission denied
error: snowflake-snowsql-1.3.1-1.x86_64: install failed
(base) dhankar@dhankar-1:~/.../config$ 
(base) dhankar@dhankar-1:~/.../config$ ls -lahtr
total 75M
-rw-rw-r-- 1 dhankar dhankar  230 Nov  3 13:39 proj_cortex_.ini
drwxrwxr-x 5 dhankar dhankar 4.0K Nov  3 13:46 ..
-rw-rw-r-- 1 dhankar dhankar  27M Nov  3 14:18 snowflake-snowsql-1.3.1-1.x86_64.rpm
-rw-rw-r-- 1 dhankar dhankar  48M Nov  3 14:31 snowsql-1.3.2-linux_x86_64.bash
drwxrwxr-x 2 dhankar dhankar 4.0K Nov  3 14:32 .
(base) dhankar@dhankar-1:~/.../config$ 

(base) dhankar@dhankar-1:~/.../config$ 
(base) dhankar@dhankar-1:~/.../config$ bash snowsql-1.3.2-linux_x86_64.bash 
**********************************************************************
 Installing SnowSQL, Snowflake CLI.
**********************************************************************

Specify the directory in which the SnowSQL components will be installed. [~/bin] 
Do you want to add /home/dhankar/bin to PATH in /home/dhankar/.profile? [y/N] y
Updating /home/dhankar/.profile to have /home/dhankar/bin in PATH
Open a new terminal session to make the updated PATH take effect.
**********************************************************************
 Congratulations! Follow the steps to connect to Snowflake DB.
**********************************************************************

1. Open a new terminal window.
2. Execute the following command to test your connection:
      snowsql -a <account_name> -u <login_name>

      Enter your password when prompted. Enter !quit to quit the connection.

3. Add your connection information to the ~/.snowsql/config file:
      accountname = <account_name>
                username = <login_name>
                password = <password>

4. Execute the following command to connect to Snowflake:

      snowsql

See the Snowflake documentation <https://docs.snowflake.net/manuals/user-guide/snowsql.html> for more information.
(base) dhankar@dhankar-1:~/.../config$ 

####

rwxr-xr-x  1 dhankar dhankar  17M Mar  1  2024 libpython3.8.so.1.0
-rwxr-xr-x  1 dhankar dhankar 976K Aug  8 16:18 _cffi_backend.cpython-38-x86_64-linux-gnu.so
-rw-r--r--  1 dhankar dhankar  426 Aug  8 16:18 snowsql.pubkey
-rw-r--r--  1 dhankar dhankar 2.9K Aug  8 16:18 snowsql.cnf
-rw-r--r--  1 dhankar dhankar 778K Aug  8 16:18 base_library.zip
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 wheel-0.44.0.dist-info
-rwxr-xr-x  1 dhankar dhankar 6.2M Aug  8 16:18 snowsql
drwxr-xr-x  3 dhankar dhankar 4.0K Aug  8 16:18 pytz
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 lib-dynload
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 keyring-23.1.0.dist-info
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 importlib_metadata-8.2.0.dist-info
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 cryptography-42.0.8.dist-info
drwxr-xr-x  3 dhankar dhankar 4.0K Aug  8 16:18 cryptography
drwxr-xr-x  8 dhankar dhankar 4.0K Aug  8 16:18 Cryptodome
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 charset_normalizer
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 certifi
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 encodings
drwxr-xr-x  2 dhankar dhankar 4.0K Aug  8 16:18 collections
drwxrwxr-x  3 dhankar dhankar 4.0K Nov  3 14:36 ..
-rw-rw-r--  1 dhankar dhankar    0 Nov  3 14:36 ok
drwxrwxr-x 14 dhankar dhankar 4.0K Nov  3 14:36 .
(base) dhankar@dhankar-1:~/.../1.3.2$ 
(base) dhankar@dhankar-1:~/.../1.3.2$ pwd
/home/dhankar/.snowsql/1.3.2
(base) dhankar@dhankar-1:~/.../1.3.2$ 


```

- snowsql -a <account_name> -u <login_name> 


#

<br/>


#### Error_1 

```shell
---CONN_urllib3__CONN-- <socket.socket fd=14, family=2, type=1, proto=6, laddr=('192.168.1.2', 56678), raddr=('20.207.203.41', 443)>
---CONN_urllib3__CONN--- <class 'socket.socket'>
2024-11-03 18:51:31.168 Uncaught app exception
Traceback (most recent call last):
  File "/home/dhankar/anaconda3/envs/env_llama_idx/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
  File "/home/dhankar/temp/08_24/proj_snow_cortex/src/st_app/sn_cortex.py", line 171, in <module>
    process_message(prompt=user_input)
  File "/home/dhankar/temp/08_24/proj_snow_cortex/src/st_app/sn_cortex.py", line 105, in process_message
    response = send_message(prompt=prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dhankar/temp/08_24/proj_snow_cortex/src/st_app/sn_cortex.py", line 88, in send_message
    raise Exception(
Exception: Failed request (id: b7eb378e-99cd-40b3-8293-bb95fe9fb822) with status 404: {
  "message" : "File revenue_timeseries.yaml not found in stage CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.RAW_DATA",
  "code" : null,
  "error_code" : "390404",
  "request_id" : "b7eb378e-99cd-40b3-8293-bb95fe9fb822"
}
['sn_cortex.py', '', '/home/dhankar/anaconda3/envs/env_llama_idx/bin', '/home/dhankar/anaconda3/envs/env_llama_idx/lib/python312.zip', '/home/dhankar/anaconda3/envs/env_llama_idx/lib/python3.12', '/home/dhankar/anaconda3/envs/env_llama_idx/lib/python3.12/lib-dynload', '/home/dhankar/anaconda3/envs/env_llama_idx/lib/python3.12/site-packages', '/home/dhankar/temp/08_24/proj_snow_cortex/src/', '/home/dhankar/temp/08_24/proj_snow_cortex/src/', '/home/dhankar/temp/08_24/proj_snow_cortex/src/']
```


#### Error_2

```shell
  File "/home/dhankar/temp/08_24/proj_snow_cortex/src/st_app/sn_cortex.py", line 88, in send_message
    raise Exception(
Exception: Failed request (id: 848795ca-17b3-4550-882e-6e13471507ad) with status 400: {
  "message" : "The required LLMs for Cortex Analyst are not available in your region. Please enable cross region calls to use this API.",
  "code" : null,
  "error_code" : "390400",
  "request_id" : "848795ca-17b3-4550-882e-6e13471507ad"
}


```


- Probable soln - [CORTEX_ENABLED_CROSS_REGION](https://docs.snowflake.com/en/sql-reference/parameters#label-cortex-enable-cross-region)


- Probable soln - [ENABLE_CORTEX_ANALYST_MODEL_AZURE_OPENAI](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst#enabling-use-of-azure-openai-models)
The ENABLE_CORTEX_ANALYST_MODEL_AZURE_OPENAI account parameter, if TRUE, allows Cortex Analyst to use Azure OpenAI models.

Enabling use of Azure OpenAI models
By default, Cortex Analyst is powered by Snowflake-hosted Cortex LLMs. You can, however, explicitly opt-in to allow Cortex Analyst to use the latest OpenAI GPT models, hosted by Microsoft Azure, alongside the Snowflake-hosted models. At runtime, Cortex Analyst selects the optimal combination of models to ensure the highest accuracy and performance for each query.





<br/>




#### Error_3

```shell

```
#### Error_4

```shell

```
#### Error_5

```shell

```
#### Error_6

```shell

```
