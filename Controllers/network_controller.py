from DB.insert_into_db import insert_network_into_db, insert_device_into_db, insert_device_connection_into_db
from File_Handler.file_handler import read_file


def make_network(pcap_file, client_id, date_taken, premise, technician_name):
    conversations = await read_file(pcap_file)
    insert_network = await insert_network_into_db(client_id, premise, date_taken)
    network_id =1#????????
    insert_devices = await insert_device_into_db(conversations, network_id)
    insert_device_connection = await insert_device_connection_into_db(conversations, network_id)
    # insert_user_network = insert_user_client(user_id, client_id)
    return insert_devices and insert_device_connection and insert_network


def get_network(network_id):
    pass