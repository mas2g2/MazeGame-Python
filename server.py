import socket
from _thread import *
import sys

server = socket.gethostbyname(socket.gethostname())
port = 5555

socketCon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketCon.bind((server, port))
except socket.error as e:
    str(e)


socketCon.listen(2)
print("Waiting for Socket Connection\n")
print("Maze Game Server Started\n\n")



def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = "hellofirst "
    while True:
        try:
            data = conn.recv(2048).decode
            if not data:
                print("Disconnected")
                break
            else:
                if player == 0:
                    reply = "a"

                else:
                    reply = "i am player 2"


            print(reply)
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = socketCon.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer = currentPlayer + 1