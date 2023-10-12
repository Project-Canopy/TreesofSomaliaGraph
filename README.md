# TreesofSomaliaGraph
Summarizes Tables 1-6 of Mahony's 1991 'Trees of Somalia' as a graph using TypeDB

# Installation
For reference, please refer to https://typedb.com/docs/typedb/2.x/overview.html\
The process for MacOS is as below:
- Install TypeDB Core: brew install typedb
- Start the server through terminal: typedb server
- Install TypeDB Studio: https://typedb.com/docs/clients/2.x/resources/downloads#_typedb_studio

# Steps for deployment
- Once installed, we will need our schema and data files.
- On TypeDB Studio, connect to TypeDB server through "Connect to TypeDB" on the bottom left.
- Open the project and select/create our database, from the option on top right corner.
- Once we have our database created, we initialize the schema by selecting schema and write options on the taskbar. Run the schema file and commit it.
- To write our data, run the data file and commit it.
- This will create our TypeDB database.
- The query file has some example queries mentioned which you can run to verify working of our code. Change our modes to data and read and run the query file to execute a query.

# Connecting with driver
- For this, we are using TypeDB Python Driver. In layman's term, this will connect our python code to the TypeDB database and we can query our database from the python code itself.
- Install typedb-driver: pip3 install typedb-driver
- Install typedb-client: pip3 install typedb-client
- Run the client.py code

# Web app
[Coming Soon!!]

