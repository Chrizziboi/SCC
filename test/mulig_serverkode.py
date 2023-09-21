import socket
from threading import Thread

# server ip adress
Server_Host = "0.0.0.0"
Server_Port = 5002
separator_token = "<SEP>"

# initialize list/set of all connected client's sockets
client_sockets = set()
#TCP socket
S = socket.socket()
#setting port as reusable
S.setsockopt(socket.sql_socket, socket.so_reuseaddr, 1)
#bind socket to specified address
S.bind((Server_Host, Server_Port))
#listen for upcoming connections
S.listen(S)
print(f"[*] Listening as {Server_Host}:{Server_Port}")

