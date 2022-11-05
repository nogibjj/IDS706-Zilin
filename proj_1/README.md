# IDS706-Zilin Project

### How to run

Docker build to build the image
```
docker build -t <IMAGE> .  
```

Docker run to start the server
```
docker run -d --name <NAME> -p <DOCKER_PORT>:<HOST_PORT> <IMAGE>
```

## Setup auth

[databricks-python](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api)

Place in Codespace secrets
* [unix, linux, mac](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api#unixlinuxandmacos)

```bash
DATABRICKS_HOST
DATABRICKS_TOKEN
```


## Test out CLI

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```
## Remote connect

[databricks-connect](https://docs.databricks.com/dev-tools/databricks-connect.html)

## Databricks SQL Connector

[Setup table first!](https://docs.databricks.com/dbfs/databricks-datasets.html)

[sql remote](https://docs.databricks.com/dev-tools/python-sql-connector.html)
https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#connection-details-cluster
