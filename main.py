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
    # if no tables, make ag table and data packet table
    # if airgradient not in table, insert
    # data packet for each air gradient
    # update master and ag when insert_datapacket
    conn = connect("master")
    cursor = conn.cursor()



    with connect("master") as conn:
        cursor = conn.cursor()
        data = server.get_data("192.168.x.x", 4000)
        insert_datapacket(cursor, data["id"], data["wifi"],
                           data["rco2"], data["pm01"], data["pm02"],
                             data["pm10"], data["pm003_count"], data["tvoc_index"], 
                             data["nox_index"], data["atmp"], data["rhum"])
        cursor.close()
