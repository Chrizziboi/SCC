import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init


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

client_socket.connect((server_host, server_port))
print(f"Koblet til: {server_host}.")

client_name = input("Skriv inn ditt navn: ")
print(f"Velkommen til Chatte-rommet, {client_name}.")

#method for listening to messages from server
def listen_for_msg():
    while True:

        def rot13dec(msg):
            str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
            str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
            str12 = msg.maketrans(str2, str1)

            return msg.translate(str12)

        msg = client_socket.recv(1024).decode()
        print("\n" + rot13dec(msg))

#making a thread that listens for msg to client
t = Thread(target=listen_for_msg)
t.daemon = True
t.start()


while True:

    msg = input(": ")

    #encoding function
    def rot13enc(msg):

        str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
        str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
        str12 = msg.maketrans(str1, str2)

        return msg.translate(str12)

    #q for ending program
    if msg.lower() == 'q':
        break
    #preparing message to send, adding current date, color and joining it together with
    #client_name message and then encrypting and sending message with client_socket.send
    date_now = datetime.now().strftime('%Y\%m\%d %H:%M:%S')
    msg_send = f" {client_color} [{date_now}] {client_name} : {msg} {Fore.RESET}"
    client_socket.send(rot13enc(msg_send).encode())

client_socket.close()