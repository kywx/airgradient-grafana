# takes the data and sorts it into a table
# in the mini processor



# database
import sqlite3
import datetime  # datetime.datetime.now



def connect(name):
    """ If database does not exist, then it'll be created 
        returns a cursor to the database """
    return sqlite3.connect(f'{name}.db')


"""
cursor.execute(query)
result = cursor.fetchall()
result = cursor.fetchone()

sqliteConnection.commit()
cursor.close()

try
except sqlite3.Error
finally
if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

with conn: context manager would be nice too
"""

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


def insert_datapacket(cursor, ag_id, wifi, rco2, pm01, pm02, pm10, pm003, tvoc, nox, atmp, rhum, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" INSERT INTO DataPacket 
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
    params = (ag_id, time, wifi, rco2, pm01, pm02, pm10, pm003, tvoc, nox, atmp, rhum)
    cursor.execute(query, params)


def update_master(cursor, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" UPDATE Master Set updated_at = ?"""
    cursor.execute(query, (time,))


def update_ag(cursor, ag_id, time=datetime.datetime.now().replace(microsecond=0)):
    query = f""" UPDATE AirGradient Set updated_at = ? WHERE ag_id = ?"""
    cursor.execute(query, (time, ag_id))


def drop_table(cursor, table):
    query = f""" Drop TABLE {table} """
    cursor.execute(query)


def truncate_table(cursor, table):
    query = f""" DELETE FROM {table} """
    cursor.execute(query)


#if __name__ == "__main__":
    #conn = connect("master")
    #cursor = conn.cursor()

    # cursor.execute("""Drop TABLE DataPacket""")

    # create_data_packet_table(cursor)

    # insert_datapacket(cursor, 1, -54, 707, 7, 13, 14, 1455, 104, 1, 20.59, 66)


    # cursor.execute("""Select * from DataPacket""")
    # print(cursor.fetchall())
    
    #conn.commit()
    #cursor.close()
    #conn.close()