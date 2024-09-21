# connect to the air gradient and extract data
# in the mini processor

"""
{"id":xxxxxx, "wifi":-59, "rco2":547, "pm01":9, "pm02":16, "pm10":17, "pm003_count":1536, "tvoc_index":0, "nox_index":0, "atmp":26.27, "rhum":60}
    this is what the data looks like
"""


import socket
import json


def get_data(HOST, PORT) -> dict:
    # sets up a server to collect data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))

        try:
            s.settimeout(15)
            s.listen(3)
            conn, addr = s.accept()
            # create a thread for the clients
            s.settimeout(None)
        except TimeoutError:
            return 0
        
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode("utf-8")  # receive data

            if data == '0':
                return 0    # error to log
            return json.loads(data)     # works only with one airgradient



# make a thread per airgradient connected that ask for data every 5 minutes or so
# the server keeps running to find more airgradients
# they insert into the sql database themselves and update stuff
# make sure to make locks on the updated_at (or maybe not since they all update at the same time and to different ags)
# can i even do that in python
# another problem: need to keep the client connected, but that means editing the ag code 

# OR

# connects one airgradient at a time, updates everything, then lets it go to accept the next one
# problem -> the airgradients don't form a line, so it might not be fair
# also this is slower

# OR

# connects one airgradient at a time and creates a thread for it
# the thread dies once it places the info into the sql database
# problem -> how to make sure we aren't spammed with data
    # use something similar to 429 http code


if __name__ == "__main__":
    while True:
        print(get_data("192.168.1.130", 4000))

# my wifi does not work LMAO