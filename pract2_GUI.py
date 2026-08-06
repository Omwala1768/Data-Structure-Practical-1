import tkinter as tk
from tkinter import messagebox
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")
        return self.items.pop(position)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            raise IndexError("Cannot traverse an empty stack")
        return " <- ".join(self.items)

    def __str__(self):
        return " <- ".join(reversed(self.items)) if self.items else "Stack is empty"


stack = Stack()

def update_stack():
    stack_label.config(text="Current Stack:\n" + str(stack))


def insert_item():
    try:
        item = item_entry.get()
        position = int(position_entry.get())

        stack.insert(item, position)

        messagebox.showinfo(
            "Inserted",
            f"'{item}' has been inserted at position {position}."
        )

        update_stack()

        item_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Position must be an integer.")

    except IndexError as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    try:
        position = int(position_entry.get())

        item = stack.delete(position)

        messagebox.showinfo(
            "Deleted",
            f"'{item}' has been deleted from position {position}."
        )

        update_stack()

        position_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Position must be an integer.")

    except IndexError as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Peek", "Top Item: " + stack.peek())
    except IndexError as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo("Stack", "Stack is NOT Empty")


def stack_size():
    messagebox.showinfo("Size", f"Stack Size: {stack.size()}")


def traverse_stack():
    try:
        messagebox.showinfo("Traverse", stack.traverse())
    except IndexError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Stack Operations")
root.geometry("500x620")
root.resizable(False, False)

title = tk.Label(
    root,
    text="STACK OPERATIONS",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Item").pack()

item_entry = tk.Entry(root, width=30)
item_entry.pack(pady=5)

tk.Label(root, text="Position").pack()

position_entry = tk.Entry(root, width=30)
position_entry.pack(pady=5)

tk.Button(
    root,
    text="Insert",
    width=20,
    command=insert_item
).pack(pady=5)

tk.Button(
    root,
    text="Delete",
    width=20,
    command=delete_item
).pack(pady=5)

tk.Button(
    root,
    text="Peek",
    width=20,
    command=peek_item
).pack(pady=5)

tk.Button(
    root,
    text="Is Empty",
    width=20,
    command=check_empty
).pack(pady=5)

tk.Button(
    root,
    text="Size",
    width=20,
    command=stack_size
).pack(pady=5)

tk.Button(
    root,
    text="Traverse",
    width=20,
    command=traverse_stack
).pack(pady=5)

stack_label = tk.Label(
    root,
    text="Current Stack:\nStack is empty",
    font=("Arial", 12, "bold"),
    fg="blue"
)
stack_label.pack(pady=20)

tk.Button(
    root,
    text="Exit",
    width=20,
    bg="red",
    fg="white",
    command=root.destroy
).pack()

root.mainloop()
