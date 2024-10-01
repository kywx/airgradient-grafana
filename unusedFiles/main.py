# functional terminal thing
# need to connect to the mini processor to access the sql database
from time import sleep
from sqlDB import *
import server


"""
{"id":xxxxxx, "wifi":-59, "rco2":547, "pm01":9, "pm02":16, "pm10":17, "pm003_count":1536, "tvoc_index":0, "nox_index":0, "atmp":26.27, "rhum":60}
    this is what the data looks like
"""




if __name__ == "__main__":
    # if no tables, make ag and data packet tables
    # if airgradient not in table, insert
    # update master and ag when insert_datapacket

    conn = connect("master")
    cursor = conn.cursor()

    try:
        create_data_packet_table(cursor)
    except sqlite3.OperationalError as e:
        print("already exists")
    
    try:
        create_ag_table(cursor)
    except sqlite3.OperationalError as e:
        print("already exists")
    
    try:
        create_master(cursor)
    except sqlite3.OperationalError as e:
        print("already exists")

    try:
        create_master(cursor)
    except sqlite3.OperationalError as e:
        print("already exists")

    conn.commit()
    cursor.close()
    conn.close()


    
    with connect("master") as conn:
        while True:
            cursor = conn.cursor()
            data = server.get_data("192.168.0.3", 4000)
            print(data)
            if data != 0:
                insert_datapacket(cursor, data)
            cursor.close()
            sleep(15)
