import mysql.connector
from mysql.connector import Error

HOST = "db4free.net"
USER = "hadas12"
PASSWORD = "@S2U.jDQGRNg!m5"
Database = "network_db"


def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


db_connection = create_server_connection(HOST, USER, PASSWORD, Database)


def execute_query(query, value, connection=db_connection):
    id = None
    try:
        cursor = connection.cursor()
        cursor.execute(query, value)
        connection.commit()
        id = cursor.lastrowid
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return id
