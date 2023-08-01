from scapy.libs.six import BytesIO
from mac_vendor_lookup import AsyncMacLookup, MacLookup
from scapy.all import rdpcap
import asyncio


async def read_file(capture_file_content):
    try:
        # TODO: Match cases for each type of capture files
        pcap_file = BytesIO(capture_file_content)
        packets = rdpcap(pcap_file)
        return await extract_devices_and_connections(packets)
    except FileNotFoundError:
        print(f"File not found: {capture_file_content}")
    except Exception as e:
        print(f"Error occurred: {e}")


async def get_device_vendor(mac_address):
    try:
        device_vendor = await AsyncMacLookup().lookup(mac_address)
    except KeyError as e:
        device_vendor = "UNKNOWN"
    return device_vendor


# TODO: extract_devices_and_connections from pcap_file
async def extract_devices_and_connections(packets):
    devices = {}
    connections_list = []
    devices_and_connection_list1 = []
    for packet in packets:
        if 'Ether' in packet:
            src_mac = packet['Ether'].src
            dest_mac = packet['Ether'].dst
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dest_ip = packet['IP'].dst

        if 'TCP' in packet:
            protocol = packet['TCP'].name
        elif 'UDP' in packet:
            protocol = packet['UDP'].name
        elif 'ARP' in packet:
            protocol = packet['ARP'].name
        elif 'ICMP' in packet:
            protocol = packet['ICMP'].name
        else:
            protocol = 'Unknown'

        if src_mac not in devices:
            vendor = await get_device_vendor(src_mac)
            devices[src_mac] = {'src_ip': src_ip, 'vendor': vendor}

        if dest_mac not in devices:
            vendor = await get_device_vendor(dest_mac)
            devices[src_mac] = {'src_ip': dest_ip, 'vendor': vendor}

        connection = {'src_mac': src_mac, 'dest_mac': dest_mac, 'protocol': protocol}
        if not connection in connections_list:
            connections_list.append(connection)

    devices_and_connection_list1.extend((devices, connections_list))
    return devices_and_connection_list1
