import socket

# server ip adress
Server_Host = "0.0.0.0"
Server_Port = 5002
separator_token = "<SEP>"

host = socket.gethostname()

#TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# initialize list/set of all connected client's sockets
client_sockets = set()
#bind socket to specified address
server_socket.bind((host, 1337))
#listen for upcoming connections
server_socket.listen(5)

print(f"[*] Listening as {Server_Host}:{Server_Port}")

#connect and accept from client
while True:
    connection, address = server_socket.accept()
    print(f"connection received from: {address}")
    connection.send(f"Server has linked: {connection}")

    connection.close()