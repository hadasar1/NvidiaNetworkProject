from DB.insert_into_db import insert_network_into_db, insert_device_into_db, insert_device_connection_into_db
from File_Handler.file_handler import read_file


async def make_network(pcap_file, client_id, premise, date_taken, technician_name):
    devices_and_connection_list = await read_file(pcap_file)
    network_id = await insert_network_into_db(client_id, premise, date_taken)
    devices_dict = devices_and_connection_list[0]
    connections_list = devices_and_connection_list[1]
    insert_devices = await insert_device_into_db(devices_dict, network_id)
    insert_device_connection = await insert_device_connection_into_db(connections_list)
    # return insert_devices and insert_device_connection and insert_network and network_id
    return "O.K The Network Created Successfully!"


def get_network(network_id):
    pass
