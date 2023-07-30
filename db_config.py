''' configuration file for database '''
import os
from langchain.vectorstores.pgvector import PGVector


# PGVector needs the connection string to the database.
CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
    host=os.environ.get("PGVECTOR_HOST", "localhost"),
    port=int(os.environ.get("PGVECTOR_PORT", "5432")),
    database=os.environ.get("PGVECTOR_DATABASE", "mydb"),
    user=os.environ.get("PGVECTOR_USER", "postgresdb"),
    password=os.environ.get("PGVECTOR_PASSWORD", "root"),
)
