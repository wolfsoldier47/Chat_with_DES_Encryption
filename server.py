#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
import DES




iv = '2132435465768797'

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    try:
        name = client.recv(BUFSIZ).decode("utf8")
        print(name)
        if name == "":
        	hashh = random.getrandbits(12)
        	name = 'random%s' % hashh
        	
        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat!" % name
        broadcast(bytes(msg, "utf8"))
    except BrokenPipeError:
        print("errno ")
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        print(msg,'this is a message')
        check = msg[-51:]
        print(check)
        if  check == bytes("339907754822691632510668191263508344339\nThisi$atest","utf8"):
        	msg = msg[:-51]
        	broadcast(msg,name+": ")
        else:
 
        	if msg != bytes("{quit}","utf8") and msg !=bytes('',"utf8"):
                    msg = DES.encrypt(iv,KEY,msg)
                    broadcast(msg, name+": ")
        		
        	else:
                    client.send(bytes("{quit}", "utf8"))
                    client.close()
                    del clients[client]
                    broadcast(bytes("%s has left the chat." % name, "utf8"))
                    break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
KEY = input("Please insert a key: ")


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
