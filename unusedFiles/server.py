# connect to the air gradient and extract data
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
