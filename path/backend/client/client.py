import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

#colors for chat
init()
colors = [Fore.BLUE, Fore.GREEN, Fore.RED]
client_color = random.choice(colors)

#creating client socket
client_socket = socket.socket()

server_host = "0.0.0.0"
server_port = 1337
separator_token = "<SEP>"

host = socket.gethostname()
port = 1337

#method for listening to messages from server
def listen_msg():
    while True:
        message = client_socket.recv(1024).decode()
        print("\n" + message)
t = Thread(target=listen_msg)
t.daemon = True
t.start()

client_socket.connect((host, port))
print(client_socket.recv(1024))
print("connected")