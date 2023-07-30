import pyshark
from scapy.layers.l2 import Ether
from tkinter import filedialog
from scapy.utils import rdpcap


async def upload_file():
    pcap_file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("pcap", "*.pcap"), ("all files", "*.*")))
    pcap_file = rdpcap(pcap_file_path)
    return pcap_file


async def read_file(pcap_file):
    capture = pyshark.FileCapture(pcap_file)
    conversations = []
    for packet in capture:
        results = read_packet(packet)
        if results is not None:
            conversations.append(results)
    return conversations


def read_packet(packet):
    try:
        protool = packet.transport_layer
        source_address = packet.ip.src
        source_port = packet[packet.transport_layer].srcport
        destination_address = packet.ip.dst
        destination_port = packet[packet.transport_layer].dstport
        source_mac = packet[Ether].src
        destination_mac = packet[Ether].dst
        packet_dict = {'protool': protool, 'source_address': source_address, 'source_port': source_port,
                       'destination_address': destination_address, 'destination_port': destination_port,
                       'source_mac': source_mac, 'destination_mac': destination_mac}
        return packet_dict
        # return (
        #     f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port} | Source MAC: {source_mac} | Destination MAC: {destination_mac}')
    except AttributeError as e:
        pass

# def network_conversation(packet):
#     try:
#         protocol = packet.transport_layer
#         source_address = packet.ip.src
#         source_port = packet[packet.transport_layer].srcport
#         destination_address = packet.ip.dst
#         destination_port = packet[packet.transport_layer].dstport
#         return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
#     except AttributeError as e:
#         pass

# pcap_file = 'test.pcap'
# capture = pyshark.FileCapture(pcap_file)
# conversations = []
# for packet in capture:
#   results = network_conversation(packet)
#   if results != None:
#     conversations.append(results)
#
# # this sorts the conversations by protocol
# # TCP and UDP
# for item in sorted(conversations):
#   print (item)


#
# import pyshark
# async def read_file(pcap_file):
#     cap = pyshark.FileCapture(r'C:\Temp\Samp1.pcap')
#     a = []
#     for i in cap:
#         try:
#             print(i['TCP'].srcport)
#             a.append(i['TCP'].srcport)
#         except:
#             print('None')
#             a.append(0)
#     pass
