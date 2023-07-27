from mysql.connector import Error
from connect_DB import db_connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def create_device(ip,mac,network_id):
    connection = db_connection()
    new_device="""
    INSERT INTO Device (ip,mac,network_id)
    VALUES (ip,mac,network_id);
    """
    execute_query(connection,new_device)

#todo insert_device_into_db
def insert_device_into_db(ip,mac,network_id):
    try:
        create_device(ip,mac,network_id)
    except Error as err:
        print(f"Error: '{err}'")


#TODO insert_device_connection_into_db
def insert_device_connection_into_db(pcap_file):
    for packet in pcap_file:
        print packet[IPv6].src
    pass


from scapy.all import *

scapy_cap = rdpcap('file.pcap')
for packet in scapy_cap:
    print packet[IPv6].src



import pyshark

cap = pyshark.FileCapture('dnpdataset')

pkts=rdpcap("MyFile.pcap")
def parsePcap():
    IPList = []
    for pkt in pkts:
        if IP in pkt:
            ip_src=pkt[IP].src
            ip_dst=pkt[IP].dst
            ip_proto=pkt[IP].proto
       IPList.append((ip_src,ip_dst,ip_proto))
    return IPList


#parseOutput = parsePcap()

# f = open('filename', 'w')
# f.write(' '.join(map(str, parsePcap())))
# f.close()

