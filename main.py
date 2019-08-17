import atexit
import json
import psycopg2
from typing import Optional


def read_xml() -> json:
    json_path: str = './people.json'
    json_str: str = open(json_path, 'r').read()

    json_obj: json = json.loads(json_str)
    return json_obj


def con() -> psycopg2:
    conn: psycopg2 = \
        psycopg2.connect(user='admin', password='', host='127.0.0.1', port='5432', database='misc')

    def clean_up() -> None:
        conn.close()
        print('Closing connection', conn)

    atexit.register(clean_up)
    return conn

