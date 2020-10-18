import socket
from _thread import *
import sys


server = "ENTER YOUR IP"  #initialize as a string
port = 5555  #intialize as an integer 

#set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prototype code to create a game
#dynamic variables
#balls = []
#height = 500
#width = 500

#1
#bind server to socket
try: 
    s.bind((server, port))
except socket.error as e:
    str(e)

#open up the port and look for set amount of connections
s.listen(2)
print("Waiting for conection")


def read_pos(str):
    if str is not None:
        str = str.split(",")
        return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#prototype Code for a game
"""
def create_balls(balls, n):
    for i in range(n):
        while True:
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            
            if stop:
                break

        balls.append((x, y, (0, 0, 0)))
"""

pos = [(0,0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))

    reply = ""
    while True:
        try: 
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            #reply = data.decode("utf-8") #make incoming data readable

            if not data:
                print("Disconnected")
                break
            else: 
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recieved: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
