import tkinter as tk
from tkinter import messagebox

SIZE = 10
hash_table = [None] * SIZE

def hash_function(key):
    return key % SIZE

def insert():
    try:
        key = int(key_entry.get())
        value = value_entry.get()

        if value == "":
            messagebox.showwarning("Warning", "Please enter a value.")
            return

        index = hash_function(key)

        if hash_table[index] is None:
            hash_table[index] = (key, value)
            messagebox.showinfo("Success", "Key inserted successfully.")
        else:
            messagebox.showerror("Error", "Collision occurred. Index already occupied.")

        display_table()

    except ValueError:
        messagebox.showerror("Error", "Key must be an integer.")

def delete():
    try:
        key = int(key_entry.get())
        index = hash_function(key)

        if hash_table[index] is not None and hash_table[index][0] == key:
            hash_table[index] = None
            messagebox.showinfo("Success", "Key deleted successfully.")
        else:
            messagebox.showerror("Error", "Key not found.")

        display_table()

    except ValueError:
        messagebox.showerror("Error", "Key must be an integer.")

def display_table():
    output.delete("1.0", tk.END)

    output.insert(tk.END, "INDEX\tKEY\tVALUE\n")
    output.insert(tk.END, "-" * 35 + "\n")

    for i in range(SIZE):
        if hash_table[i] is not None:
            key, value = hash_table[i]
            output.insert(tk.END, f"{i}\t{key}\t{value}\n")
        else:
            output.insert(tk.END, f"{i}\t-\t-\n")

def clear_fields():
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Hash Table - Om Wala S119")
root.geometry("650x600")
root.configure(bg="#F4F6F8")

title = tk.Label(
    root,
    text="Hash Table",
    font=("Segoe UI", 24, "bold"),
    bg="#F4F6F8",
    fg="#333333"
)
title.pack(pady=15)

student = tk.Label(
    root,
    text="Om Wala S119",
    font=("Segoe UI", 12, "bold"),
    bg="#F4F6F8",
    fg="#4A90E2"
)
student.pack()

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=20)

tk.Label(
    frame,
    text="Key:",
    font=("Segoe UI", 12),
    bg="white"
).grid(row=0, column=0, padx=10, pady=10)

key_entry = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=25
)
key_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(
    frame,
    text="Value:",
    font=("Segoe UI", 12),
    bg="white"
).grid(row=1, column=0, padx=10, pady=10)

value_entry = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=25
)
value_entry.grid(row=1, column=1, padx=10, pady=10)

insert_button = tk.Button(
    frame,
    text="Insert",
    font=("Segoe UI", 11, "bold"),
    bg="#4A90E2",
    fg="white",
    width=12,
    command=insert
)
insert_button.grid(row=2, column=0, padx=5, pady=15)

delete_button = tk.Button(
    frame,
    text="Delete",
    font=("Segoe UI", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    width=12,
    command=delete
)
delete_button.grid(row=2, column=1, padx=5, pady=15)

clear_button = tk.Button(
    frame,
    text="Clear",
    font=("Segoe UI", 11, "bold"),
    bg="#50C878",
    fg="white",
    width=12,
    command=clear_fields
)
clear_button.grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(
    root,
    text="Hash Table Traversal",
    font=("Segoe UI", 15, "bold"),
    bg="#F4F6F8",
    fg="#333333"
).pack(pady=5)

output = tk.Text(
    root,
    font=("Consolas", 12),
    width=55,
    height=13
)
output.pack(pady=10)

display_table()

root.mainloop()
