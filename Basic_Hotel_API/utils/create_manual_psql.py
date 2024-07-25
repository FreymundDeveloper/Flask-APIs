import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

def create_database_psql():
    db_host = os.getenv('DB_HOST', os.getenv('LOCALHOST'))
    db_port = os.getenv('DB_PORT', os.getenv('PORT'))
    db_user = os.getenv('DB_USER', os.getenv('USER'))
    db_password = os.getenv('DB_PASSWORD', os.getenv('PASSWORD'))
    db_name = os.getenv('DB_NAME', os.getenv('DATABASE'))

    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name))
            )
            print(f"Database '{db_name}' created.")
        else:
            print(f"Database '{db_name}' already exists.")

        cursor.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()