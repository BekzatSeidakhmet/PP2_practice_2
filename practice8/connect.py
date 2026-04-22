import psycopg
from config import host, database, user, password, port


def connect():
    conn = psycopg.connect(
        host=host,
        dbname=database,
        user=user,
        password=password,
        port=port
    )
    return conn