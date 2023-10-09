import socket
from threading import Thread
import cryptography

def main():
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
    print(f"[*] Listening as {server_host}: {server_port}")

    #method for connect and accept/decline from client
    def  client_handler(client):

        while True:
            #listen for clients
            try:
                msg = client.recv(1024).decode()
                if not msg:
                    break
                #disconnecting client
                #removing client from set
            except Exception as e:
                print(f"[!] Error: {e}.")
                client_sockets.remove(client)
                break
            else:
                msg = msg.replace(separator_token, ":")
            for x in client_sockets:
                x.send(msg.encode())

    #listen for new connections, add clients and start a new thread for msg
    while True:

        client_socket, address = server_socket.accept()
        print(f" {address} :connected successfully")
        client_sockets.add(client_socket)
        t = Thread(target=client_handler, args=(client_socket,))
        t.daemon = True
        t.start()

    for x in client_sockets:
        x.close()
        server_socket.close()

main()


