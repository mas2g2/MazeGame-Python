import socket
from _thread import *
import sys

server = "192.168.0.233"
port = 5555

socketCon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketCon.bind((server, port))
except socket.error as e:
    str(e)


socketCon.listen(2)
print("Waiting for Socket Connection\n")
print("Maze Game Server Started\n\n")



def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


#pos = [(0, 0), (100, 100)]


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


while True:
    conn, addr = socketCon.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, ))