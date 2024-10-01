import sqlite3
import datetime  # datetime.datetime.now



def connect(name):
    """ If database does not exist, then it'll be created 
        returns a cursor to the database """
    return sqlite3.connect(f'{name}.db', isolation_level=None)


def create_master(cursor):
    query = """ CREATE TABLE Master (
                created_at DATETIME NOT NULL,
                updated_at DATETIME NOT NULL
                ); """
    cursor.execute(query)


def create_ag_table(cursor):
    query = """ CREATE TABLE AirGradient (
                ag_id varchar(255) NOT NULL PRIMARY KEY,
                location_name varchar(255),
                created_at DATETIME,
                updated_at DATETIME
                ); """
    cursor.execute(query)


def create_data_packet_table(cursor):
    query = """ CREATE TABLE DataPacket (
                ag_id varchar(255) NOT NULL,
                timestamp DATETIME NOT NULL,
                wifi INTEGER,
                rco2 INTEGER,
                pm01 INTEGER,
                pm02 INTEGER,
                pm10 INTEGER,
                pm003_count INTEGER,
                tvoc_index INTEGER,
                nox_index INTEGER,
                atmp INTEGER,
                rhum INTEGER,
                FOREIGN KEY (ag_id) REFERENCES AirGradient(ag_id)
                ); """
    cursor.execute(query)


def insert_airgradient(cursor, ag_id, name, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" INSERT INTO AirGradient
                VALUES (?,?,?,?);"""
    params = (ag_id, name, time, time)
    cursor.execute(query, params)



def insert_datapacket(cursor, data, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" INSERT INTO DataPacket 
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
    params = (data["id"], time, data["wifi"], data["rco2"], data["pm01"], data["pm02"], data["pm10"], data["pm003_count"], data["tvoc_index"], data["nox_index"], data["atmp"], data["rhum"])
    cursor.execute(query, params)
    
    # check if air gradient exists in the table
    cursor.execute("""Select ag_id from AirGradient""")
    all = [row[0] for row in cursor]
    if data["id"] not in all:
        insert_airgradient(cursor, data["id"], data["id"])
    
    # update updated_at
    update_ag(cursor, data["id"])
    update_master(cursor)



def update_master(cursor, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" UPDATE Master Set updated_at = ?"""
    cursor.execute(query, (time,))


def update_ag(cursor, ag_id, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" UPDATE AirGradient Set updated_at = ? WHERE ag_id = ?"""
    cursor.execute(query, (time, ag_id))


def update_location_name(cursor, name, ag_id):
    query = f""" UPDATE AirGradient Set location_name = ? WHERE ag_id = ?"""
    cursor.execute(query, (name, ag_id))


def drop_table(cursor, table):
    query = f""" Drop TABLE {table} """
    cursor.execute(query)


def truncate_table(cursor, table):
    query = f""" DELETE FROM {table} """
    cursor.execute(query)
