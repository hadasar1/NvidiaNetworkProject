from DB.query import execute_query

user_table = """
CREATE TABLE User(
id INT PRIMARY KEY AUTO_INCREMENT,
name NVARCHAR(50),
password NVARCHAR(50))
"""

# execute_query(user_table)

insert_user = """
INSERT INTO User
(name, password)
VALUES('Shalom','66674321')
"""
# execute_query(insert_user)

insert_user1 = """
INSERT into User
(name, password)
VALUES('Chaim','74657385')
"""
# execute_query(insert_user1)

insert_user3 = """
INSERT into User
(name, password)
VALUES('David','12345678'),('Beni','95847365')
"""
# execute_query(insert_user3)

client_table = """
CREATE TABLE Client(
id INT PRIMARY KEY AUTO_INCREMENT,
name NVARCHAR(50))
"""
# execute_query(client_table)
user_client_table = """
CREATE TABLE User_Client(
id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
FOREIGN KEY(user_id) REFERENCES User(id),
client_id INT NOT NULL,
FOREIGN KEY(client_id) REFERENCES Client(id)
)
"""
# execute_query(user_client_table)

network_table = """
CREATE TABLE Network(
id INT PRIMARY KEY AUTO_INCREMENT,
client_id INT,
FOREIGN KEY(client_id) REFERENCES Client(id),
premise NVARCHAR(50),
date_taken DATE)
"""

# execute_query(network_table)

device_table = """
CREATE TABLE Device(
id INT PRIMARY KEY AUTO_INCREMENT,
ip NVARCHAR(50),
mac NVARCHAR(50),
vendor NVARCHAR(50),
network_id INT,
FOREIGN KEY(network_id) REFERENCES Network(id)
)
"""
# execute_query(device_table)

device_connections_table = """
CREATE TABLE Device_Connections_table(
id INT PRIMARY KEY AUTO_INCREMENT,
src_mac NVARCHAR(50),
dest_mac NVARCHAR(50),
protocol NVARCHAR(50)
)
"""

# execute_query(device_connections_table)

new_device = """
   INSERT INTO Device (ip,mac,network_id)
   VALUES (ip,mac,network_id);
   """

client_details = """
INSERT into Client
(name)
VALUES('Moshe');
"""
# execute_query(client_details)

#
# def create_user(name, password):
#     execute_query(db_connection, """
# INSERT into User
# (name, password)
# VALUES(%s, %s)
# val = (name, password)
# """)

# execute_query(db_connection, create_user('Dani', '55555555'))


































def create_user(name, password):
    execute_query(db_connection, """
INSERT into User
(name, password)
VALUES(%s, %s)
val = (name, password)
""")


# execute_query(db_connection, create_user('Dani', '55555555'))
