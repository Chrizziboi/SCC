import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


#colors for chat
init()
#list of different colors
colors = [Fore.BLUE, Fore.GREEN, Fore.RED]
#using random to choose color from list
client_color = random.choice(colors)

#creating client socket TCP
client_socket = socket.socket()

server_host = "127.0.0.1"
server_port = 1337
separator_token = "<SEP>"

client_socket.connect((server_host, server_port))
print(f"connected to: {server_host}.")

client_name = input("Enter you name: ")
print(f"Welcome to the chat room, {client_name}.")

#method for listening to messages from server
def listen_for_msg():
    while True:
        print(client_socket.recv(1024))
        message = client_socket.recv(1024).decode()
        print("\n" + message)

#making a thread that listens for msg to client
t = Thread(target=listen_for_msg)
t.daemon = True
t.start()

while True:
    #msg to send
    msg_send = input()
    #q for ending program
    if msg_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg_send = f" {client_color} [{date_now}] {client_name} {separator_token} {msg_send} {Fore.RESET}"
    print("bug here?")
    client_socket.send(msg_send.encode())

client_socket.close()