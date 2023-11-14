import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# creating client socket TCP
server_host = "127.0.0.1"
server_port = 1337
client_socket = socket.socket()

def close():
    client_socket.close()


def listen_for_msg():
    while True:
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

def main(username):

    global chat_window, chat_box, entry
    chat_window = tk.Tk()
    chat_window.title("Chat Room")
    chat_window.configure(bg='#11242C')

    chat_box = scrolledtext.ScrolledText(chat_window, state=tk.DISABLED, wrap=tk.WORD, fg='gainsboro', bg='#11242C')
    chat_box.pack(expand=True, fill=tk.BOTH)

    entry = tk.Entry(chat_window, width=50, fg='gray20', bg='gainsboro')
    entry.pack(side=tk.LEFT, padx=10, pady=10)
    client_socket.connect((server_host, server_port))

    send_button = tk.Button(chat_window, text="Send", command=send_msg, fg='gainsboro', bg='#11242C')
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

 '''   chat_box.insert(tk.END, f"Koblet til: {server_host}.\n")
    chat_box.insert(tk.END, f"Velkommen til Chatte-rommet: {username}.\n")
    chat_box.config(state=tk.DISABLED)'''

    t = threading.Thread(target=listen_for_msg)
    t.daemon = True
    t.start()

    chat_window.mainloop()
def send_msg():

    msg = entry.get()
    if msg:
        def rot13enc(msg):
            str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
            str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
            str12 = msg.maketrans(str1, str2)
            return msg.translate(str12)

        msg_encoded = rot13enc(msg)
        client_socket.send(msg_encoded.encode())
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"{username}: {msg}\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)






login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Enter username:").pack(side="top", fill="x", pady=10)

username_entry = tk.Entry(login_window)
username_entry.pack(side="top", fill="x", padx=10)


def on_login_click():
    username = username_entry.get()
    if username:
        main(username)
        login_window.destroy()


login_button = tk.Button(login_window, text="Login", command=on_login_click)
login_button.pack(side="top", pady=10, padx=10)

login_window.protocol("WM_DELETE_WINDOW", lambda: login_window.destroy())



login_window.mainloop()
