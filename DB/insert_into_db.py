from DB.crud import create_device_connections, create_network
from mysql.connector import Error
from DB.crud import create_device


def insert_network_into_db(client_id, premise, date_taken):
    try:
        create_network(client_id, premise, date_taken)
    except Error as err:
        print(f"Error: '{err}'")
    return True


#TODO: insert_device_into_db
def insert_device_into_db(pcap_file_conversations, network_id):
    # insert ip mac network_id
    for packet in pcap_file_conversations:
        ip = packet.source_address
        mac = packet.source_mac
        try:
            create_device(ip, mac, network_id)
        except Error as err:
            print(f"Error: '{err}'")
    return True


#TODO insert_device_connection_into_db
def insert_device_connection_into_db(pcap_file_conversations, network_id):
    try:
        for packet in pcap_file_conversations:
            src = packet.source_address
            destination = packet.destination_address
            protocol = packet.protocol
            create_device_connections(src, destination, protocol, network_id)
    except Error as err:
        print(f"Error: '{err}'")
    return True


def insert_user_client(user_id, client_id):
    pass
