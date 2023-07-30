import mysql.connector
from mysql.connector import Error

HOST = "sql7.freesqldatabase.com"
USER = "sql7635081"
PASSWORD = "8hPyFfea3s"
Database = "sql7635081"


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


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return True
