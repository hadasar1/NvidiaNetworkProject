from Authentication.check_if_user_db import UserInDB
from mysql.connector import Error
from DB.query import db_connection, execute_query


async def create_device(ip, mac, vendor, network_id):
    new_device = """
    INSERT into Device (ip,mac,vendor,network_id)
    VALUES (%s, %s, %s, %s);
    """
    values = (ip, mac, vendor, network_id)
    insert_device = execute_query(new_device, values)
    return insert_device


async def create_network(client_id, premise, date_taken):
    new_network = """
        INSERT into Network (client_id,premise,date_taken)
        VALUES (%s, %s, %s);
        """
    values = (client_id, premise, date_taken)
    insert_network = execute_query(new_network, values)
    return insert_network


async def create_device_connections(src_mac, dest_mac, protocol):
    new_device_connections = """
           INSERT into Device_Connections_table (src_mac,dest_mac,protocol)
           VALUES (%s, %s, %s);
           """
    values = (src_mac, dest_mac, protocol)
    insert_device_connections = execute_query(new_device_connections, values)
    return insert_device_connections


async def create_user_client(user_id, client_id):
    new_user_client = """
            INSERT into User_Client (user_id,client_id)
            VALUES (%s, %s);
            """
    values = (user_id, client_id)
    insert_user_client = execute_query(new_user_client, values)
    return insert_user_client


# def get_all_users():
#     connection = db_connection()
#     get_users_query = "SELECT id, name, password FROM user_table;"
#     users = execute_query(connection, get_users_query).fetchall()
#     return users


def get_password_by_name(username):
    try:
        connection = db_connection()
        get_password_query = "SELECT password FROM user_table WHERE name = %s"
        cursor = connection.cursor()
        cursor.execute(get_password_query, username)
        user_data = cursor.fetchone()
        if user_data:
            user_id, username, password = user_data
            return UserInDB(name=username, id=user_id, hashed_password=password)
        else:
            return None
    except Error as e:
        print("Error:", e)
        return None


