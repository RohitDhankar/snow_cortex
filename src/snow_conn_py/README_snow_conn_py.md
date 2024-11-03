
## Snowflake Connector for Python

### Table of Contents

<br/>

#### Snowflake Connector for Python

- [1 Snowflake Python APIs: General concepts](https://docs.snowflake.com/developer-guide/snowflake-python-api/snowflake-python-general-concepts)

- [1.a) Entry point: The Root object](https://docs.snowflake.com/developer-guide/snowflake-python-api/snowflake-python-general-concepts#entry-point-the-root-object)

- The Root object is the entry point for the Python API. You create an instance of ```Root``` that is configured with the Snowflake context in which it will run, by using a Python Connector Connection object or a Snowpark Session object.

- [1.b) Account, database, and schema scopes](https://docs.snowflake.com/developer-guide/snowflake-python-api/snowflake-python-general-concepts#account-database-and-schema-scopes)
- With a Root object, you can access the collections of account-scoped objects, such as
- warehouses (root.warehouses), 
- databases (root.databases), and 
- external volumes (root.external_volumes).

<br/>

- [Root]
- [DatabaseCollection]
- [DatabaseResource]

- You can access database-scoped objects under a DatabaseResource, which in turn you can retrieve through the DatabaseCollection object under Root. 

- [1.c) SchemaResource object](https://docs.snowflake.com/developer-guide/snowflake-python-api/snowflake-python-general-concepts#account-database-and-schema-scopes)
- [SchemaCollection]

- Currently, SchemaCollection is the only object type available under the database scope.
You can access schema-scoped objects, such as tables, views, streams, and stages, through the SchemaResource object.

For example, the following code accesses a StageCollection first, and then a StageResource:
