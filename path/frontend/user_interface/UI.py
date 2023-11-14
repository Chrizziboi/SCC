import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = entry.get()
    if message:
        chat_box.config(state=tk.NORMAL, fg='gainsboro', bg='#11242C')
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

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

# Opprett sende-knappen
send_button = tk.Button(root, text="Send", command=send_message, fg='#11242C', bg='gainsboro')
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start hovedloopen
root.mainloop()