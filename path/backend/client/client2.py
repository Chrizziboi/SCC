''''import socket
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

client_socket.close()'''


'''
import socket
import threading
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext



# creating client socket TCP


server_host = "127.0.0.1"
server_port = 1337

#method for listening to messages from server
def listen_for_msg():
    while True:
        try:
            def rot13dec(msg):
                str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
                str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
                str12 = msg.maketrans(str2, str1)
                return msg.translate(str12);


            msg = client_socket.recv(1024).decode()
            chat_box.config(state=tk.NORMAL, fg='gainsboro', bg='#11242C')
            chat_box.insert(tk.END, msg + "\n")
            chat_box.config(state=tk.DISABLED)
        except ConnectionAbortedError:
            break
        except:
            print("Error receiving message")
            client_socket.close()
            break

def send_msg():
    #while True:
        #msg = input(": ")
        msg = entry2.get()

        if msg:
            #encoding function
            def rot13enc(msg):

                str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
                str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
                str12 = msg.maketrans(str1, str2)

                return msg.translate(str12)

            #q for ending program
            #if msg.lower() == 'q':
            #   break
            #preparing message to send, adding current date, color and joining it together with
            #client_name message and then encrypting and sending message with client_socket.send
            #date_now = datetime.now().strftime('%Y\%m\%d %H:%M:%S')
            #msg_send = f" [{date_now}] {client_name} : {msg}"
            msg_send = msg
            client_socket.send(rot13enc(msg_send).encode())
            #client_socket.send(bytes(msg, 'utf-8'))
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, entry.get() +": " + msg_send + "\n")
            chat_box.config(state=tk.DISABLED)
            entry.delete(0, tk.END)

client_socket = socket.socket()
# Opprett hovedvinduet
root = tk.Tk()
root.title("Chat Room")
root.configure(bg='#11242C')

# Opprett chatboksen
chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, fg='gainsboro', bg='#11242C')
chat_box.pack(expand=True, fill=tk.BOTH)

# Opprett inntastingsfeltet
entry = tk.Entry(root, width=50, fg='#11242C', bg='snow2')
entry.pack(side=tk.LEFT, padx=10, pady=10)

entry2 = tk.Entry(root, width=50, fg='#11242C', bg='snow2')
entry2.pack(side=tk.LEFT, padx=10, pady=10)

# Opprett sende-knappen
send_button = tk.Button(root, text="Send", command=send_msg, fg='#11242C', bg='gainsboro')
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

def main():
    client_socket.connect((server_host, server_port))
    # Start hovedloopen
    listen_for_msg()

    root.mainloop()


    # making a thread that listens for msg to client

    #chat_box.insert(tk.END, f"Koblet til: {server_host}.")

    #chat_box.insert(tk.END, f"Velkommen til Chatte-rommet, {client_name}.")

t = threading.Thread(target=listen_for_msg)
t.daemon = True
t.start()

main()
#making a thread that listens for main
t1 = threading.Thread(target=main)
t1.daemon = True
t1.start()


def close():
    client_socket.close()
'''




import socket
import threading
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext


def close():
    client_socket.close()
    #root.destroy()

def listen_for_msg():
    while True:
        t = threading.Thread(target=listen_for_msg)
        t.daemon = True
        t.start()
        # Start hovedloopen
        #root.mainloop()
        try:
            def rot13dec(msg):
                str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
                str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
                str12 = msg.maketrans(str2, str1)
                return msg.translate(str12)

            msg = client_socket.recv(1024).decode()
            chat_box.config(state=tk.NORMAL, fg='gainsboro', bg='#11242C')
            chat_box.insert(tk.END, rot13dec(msg) + "\n")
            chat_box.config(state=tk.DISABLED)
        except ConnectionAbortedError:
            break
        except:
            print("Error receiving message")
            client_socket.close()
            break

def send_msg():
    msg = entry.get()
    if msg:
        def rot13enc(msg):
            str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
            str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
            str12 = msg.maketrans(str1, str2)
            return msg.translate(str12)

        msg_send = msg
        client_socket.send(rot13enc(msg_send).encode())
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, entry.get() + ": " + msg_send + "\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

def main(username):
    # Opprett hovedvinduet
    root = tk.Tk()
    root.title("Chat Room")
    root.configure(bg='#11242C')

    # Opprett chatboksen
    chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, fg='gainsboro', bg='#11242C')
    chat_box.pack(expand=True, fill=tk.BOTH)

    # Opprett inntastingsfeltet
    entry = tk.Entry(root, width=50, fg='gray20', bg='gainsboro')
    entry.pack(side=tk.LEFT, padx=10, pady=10)

    # Opprett sende-knappen
    send_button = tk.Button(root, text="Send", command=send_msg, fg='gainsboro', bg='#11242C')
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    client_socket.connect((server_host, server_port))
    chat_box.insert(tk.END, f"Koblet til: {server_host}.\n")
    chat_box.insert(tk.END, f"Velkommen til Chatte-rommet: {username}.\n")
    chat_box.config(state=tk.DISABLED)

    # making a thread that listens for msg to client
'''    t = threading.Thread(target=listen_for_msg)
    t.daemon = True
    t.start()'''



'''def login():
    root2 = tk.Tk()
    root2.title("Login page")
    root2.configure(bg='#11242C')
    entry2 = tk.Entry(root2, width=50, fg='gainsboro', bg='snow2')
    entry2.pack(side=tk.LEFT, padx=10, pady=10)
    login_button = tk.Button(root2, text="Logg inn", fg='gainsboro', bg='#11242C')
    login_button.pack(side=tk.RIGHT, padx=10, pady=10)'''



'''def show_login_window():
    root2 = tk.Tk()
    login_window = tk.Toplevel(root2)
    login_window.title("Login")

    tk.Label(login_window, text="Enter username:").pack(side="top", fill="x", pady=10)

    username_entry = tk.Entry(login_window)
    username_entry.pack(side="top", fill="x", padx=10)
    client_socket.connect((server_host, server_port))
    def on_login_click():
        username = username_entry.get()
        if username:
            main(username)
            login_window.destroy()
            root2.deiconify()  # Show the main chat window

    login_button = tk.Button(login_window, text="Login", command=on_login_click)
    login_button.pack(side="top", pady=10, padx=10)
    on_login_click()

    # When the login window is closed, exit the program
    login_window.protocol("WM_DELETE_WINDOW", lambda: root2.destroy())'''

def show_login_window():
    root2 = tk.Tk()
    login_window = tk.Toplevel(root2)
    login_window.title("Login")

    tk.Label(login_window, text="Enter username:").pack(side="top", fill="x", pady=10)

    username_entry = tk.Entry(login_window)
    username_entry.pack(side="top", fill="x", padx=10)

    def on_login_click():
        username = username_entry.get()
        if username:
            main(username)
            login_window.destroy()
            root.mainloop()

    login_button = tk.Button(login_window, text="Login", command=on_login_click)
    login_button.pack(side="top", pady=10, padx=10)

    # When the login window is closed, exit the program
    login_window.protocol("WM_DELETE_WINDOW", lambda: root2.destroy())

# Hide the main window until the user logs in
#root2.withdraw()






    


# creating client socket TCP
server_host = "127.0.0.1"
server_port = 1337
client_socket = socket.socket()
'''
# Opprett hovedvinduet
root = tk.Tk()
root.title("Chat Room")
root.configure(bg='#11242C')

# Opprett chatboksen
chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, fg='gainsboro', bg='#11242C')
chat_box.pack(expand=True, fill=tk.BOTH)

# Opprett inntastingsfeltet
entry = tk.Entry(root, width=50, fg='gray20', bg='gainsboro')
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Opprett sende-knappen
send_button = tk.Button(root, text="Send", command=send_msg, fg='gainsboro', bg='#11242C')
send_button.pack(side=tk.RIGHT, padx=10, pady=10)'''


#main("Yo")
print("horebukk")

#root.withdraw()
show_login_window()
#login()
#root2.mainloop()
# making a thread that listens for main
'''t1 = threading.Thread(target=main)
t1.daemon = True
t1.start()'''

