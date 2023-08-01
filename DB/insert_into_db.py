from DB.crud import create_device_connections, create_network
from mysql.connector import Error
from DB.crud import create_device


async def insert_network_into_db(client_id, premise, date_taken):
    network_id = None
    try:
        network_id = await create_network(client_id, premise, date_taken)
        print("create network soffiiii!!!!")
    except Error as err:
        print(f"Error in insert_network_into_db: '{err}'")
    return network_id


# TODO: insert_device_into_db
async def insert_device_into_db(devices_dict, network_id):
    device_id = None
    for device, device_info in devices_dict.items():
        ip = device_info.get('src_ip')
        mac = device
        vendor = device_info.get('vendor')
        try:
            device_id = await create_device(ip, mac, vendor, network_id)
        except Error as err:
            print(f"Error - insert_device_into_db: '{err}'")
    # return device_id
    return 2


# TODO insert_device_connection_into_db
async def insert_device_connection_into_db(connections_list):
    try:
        for connection_dict in connections_list:
            src_mac = connection_dict['src_mac']
            dest_mac = connection_dict['dest_mac']
            protocol = connection_dict['protocol']
            connections_id = await create_device_connections(src_mac, dest_mac, protocol)
    except Error as err:
        print(f"Error - insert_device_connection_into_db: '{err}'")
    # return connections_id
    return 3


def insert_user_client(user_id, client_id):
    pass
