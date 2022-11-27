import psycopg2
import logging
from psycopg2 import Error

username="postgres"
pwd="32794"
hostname="localhost"
port_id="5432"
dbname="postgres"
connect = None
cur = None

try:
    connect = psycopg2.connect(
        host = hostname,
        database = dbname,
        user = username,
        port = port_id,
        password = pwd, )

    pointer = connect.cursor()
    connect.autocommit = True 

    
    create_script = ''' CREATE TABLE IF NOT EXISTS spisok(
                            text text,
                            created_date date,
                            rubrics varchar(200),
                            id serial PRIMARY KEY )'''
    
    pointer.execute(create_script)
    
    connect.commit()
    logging.info("Table is created")

except Exception as error:
    logging.error("Table this duplicated", e)

finally:
    if pointer is not None:
        pointer.close()
    if connect is not None:
        connect.close()
