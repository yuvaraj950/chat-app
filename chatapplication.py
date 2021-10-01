import socket
import select
import sys
import threading
from threading import *

server = socket .socket(socket.AF_INET , socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("correct usage: script , IP address, port number")
    exit()
Ip_address = str(sys.argv[1])
port = int(sys.argv[2])

server.bind(Ip_address,port)
server.listen(100)

list_of_client = []

def clentthread(conn,addr):
    conn.send("Welcome to this chatroom!")
    while True:
        try :
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + ">" + message)
                message_to_send = "<" + addr[0] + " > " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue
def broastcast(message, connection):
    for clients in list_of_clients:
        if clients!= connection:
            try:
                clients.send(message)
            except:
                client.close()
                remove(clients)
def remove(connection):
   if connection in list_of_clients:
       list_of_clients.remove(connection)
while True:
    conn , addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + "connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()

#client side of chat room

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv)!= 3:
    print("correct usage:script,IP adress,port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:
    sockets_list =[sys.stdin, server]
    read_socket,write_socket, error_socket = select.select(sockets_list,[] , [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<you>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()

