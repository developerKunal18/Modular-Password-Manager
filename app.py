import tkinter as tk
from tkinter import messagebox

from utils import encode, decode
from storage import load_data, save_data
from auth import setup_master, verify_password

setup_master()

def refresh():
    listbox.delete(0, tk.END)

    for line in load_data():
        account, password = line.strip().split(":")
        listbox.insert(tk.END, f"{account} → {decode(password)}")

def save_password():
    account = account_entry.get()
    password = password_entry.get()

    if account and password:
        data = load_data()
        data.append(f"{account}:{encode(password)}\n")
        save_data(data)

        account_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

        refresh()

def delete_password():
    selected = listbox.curselection()

    if selected:
        index = selected[0]

        data = load_data()
        data.pop(index)

        save_data(data)
        refresh()

def open_manager():
    global account_entry, password_entry, listbox

    root = tk.Tk()
    root.title("Modular Password Manager")

    tk.Label(root, text="Account").pack()
    account_entry = tk.Entry(root, width=40)
    account_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, width=40, show="*")
    password_entry.pack()

    tk.Button(root, text="Save", command=save_password).pack(pady=5)

    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)

    tk.Button(root, text="Delete Selected", command=delete_password).pack()

    refresh()

    root.mainloop()

def login():
    password = login_entry.get()

    if verify_password(password):
        login_window.destroy()
        open_manager()
    else:
        messagebox.showerror("Error", "Wrong password")

# Login Window
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Master Password").pack(pady=10)

login_entry = tk.Entry(login_window, show="*", width=30)
login_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)

login_window.mainloop()
