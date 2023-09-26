import socket
from threading import Thread

# server ip address
server_host = "0.0.0.0"
server_port = 1337
separator_token = "<SEP>"

#TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Making port reusable
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# initialize list/set of all connected client's sockets
client_sockets = set()
#bind socket to specified address
server_socket.bind((server_host, server_port))
#listen for upcoming connections
server_socket.listen(5)
print(f"[*] Listening as {server_host}:{server_port}")

#method for connect and accept/decline from client
def  client_handler(client):

    while True:
        try:
            msg = client.recv(1024).decode()
        except Exception as e:
            client_sockets.remove(client)
        else:
            msg = msg.replace(separator_token, ":")
        for x in client_sockets:
            x.send(msg.encode())
#listen for new connections
while True:
    connection, address = server_socket.accept()
    print(f"connection received from: {address}")
    cs = connection.encode("Server has linked")
    connection.send(cs)

'''
        #data being sent
        data = connection.recv(1024)
        if not data:
            break
        print("Received message"), repr(data)
        connection.close()
'''


#accepting connections
while True:

    for x in range(4):
        Thread(target=client_handler).start()
    client_handler()

server_socket.close()