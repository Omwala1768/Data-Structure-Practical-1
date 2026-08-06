import tkinter as tk
from tkinter import messagebox

class PriorityQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_capacity

    def enqueue(self, item, priority):
        if self.is_full():
            return "Priority Queue is Full. Cannot Enqueue."
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        return f"Enqueued: {item} with Priority {priority}"

    def dequeue(self):
        if self.is_empty():
            return "Priority Queue is Empty. Cannot Dequeue."
        item = self.queue.pop(0)
        return f"Dequeued: {item[0]}"

    def traverse(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        text = "Priority Queue Contains:\n\n"
        for item, priority in self.queue:
            text += f"Item: {item}    Priority: {priority}\n"
        return text

    def ascending_order(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        text = "Ascending Order:\n\n"
        for item, priority in sorted(self.queue, key=lambda x: x[1]):
            text += f"Item: {item}    Priority: {priority}\n"
        return text

    def descending_order(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        text = "Descending Order:\n\n"
        for item, priority in sorted(self.queue, key=lambda x: x[1], reverse=True):
            text += f"Item: {item}    Priority: {priority}\n"
        return text

pq = None

def create_queue():
    global pq
    try:
        size = int(size_entry.get())
        if size <= 0:
            raise ValueError
        pq = PriorityQueue(size)
        display("Priority Queue Created Successfully\nMaximum Capacity = {}".format(size))
    except:
        messagebox.showerror("Error", "Enter a Valid Queue Capacity")

def display(text):
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)

def enqueue():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    item = item_entry.get()
    if item == "":
        messagebox.showerror("Error", "Enter Item")
        return
    try:
        priority = int(priority_entry.get())
        display(pq.enqueue(item, priority))
    except:
        messagebox.showerror("Error", "Priority Must be an Integer")

def dequeue():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    display(pq.dequeue())

def traverse():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    display(pq.traverse())

def ascending():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    display(pq.ascending_order())

def descending():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    display(pq.descending_order())

def check_empty():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    if pq.is_empty():
        display("Priority Queue is Empty")
    else:
        display("Priority Queue is Not Empty")

def check_full():
    if pq is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    if pq.is_full():
        display("Priority Queue is Full")
    else:
        display("Priority Queue is Not Full")

root = tk.Tk()
root.title("Om Wala S119 - Priority Queue")
root.geometry("850x700")
root.configure(bg="#EAF4FC")

title = tk.Label(
    root,
    text="Om Wala S119\nPriority Queue Operations",
    font=("Arial", 20, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

top = tk.Frame(root, bg="#EAF4FC")
top.pack(pady=15)

tk.Label(top, text="Queue Capacity", font=("Arial", 12, "bold"), bg="#EAF4FC").grid(row=0, column=0, padx=10, pady=10)
size_entry = tk.Entry(top, font=("Arial", 12), width=15)
size_entry.grid(row=0, column=1)

tk.Button(top, text="Create Queue", font=("Arial", 11, "bold"), bg="#43A047", fg="white", width=15, command=create_queue).grid(row=0, column=2, padx=10)

tk.Label(top, text="Item", font=("Arial", 12, "bold"), bg="#EAF4FC").grid(row=1, column=0, padx=10, pady=10)
item_entry = tk.Entry(top, font=("Arial", 12), width=15)
item_entry.grid(row=1, column=1)

tk.Label(top, text="Priority", font=("Arial", 12, "bold"), bg="#EAF4FC").grid(row=2, column=0, padx=10, pady=10)
priority_entry = tk.Entry(top, font=("Arial", 12), width=15)
priority_entry.grid(row=2, column=1)

button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=10)

buttons = [
    ("Enqueue", enqueue),
    ("Dequeue", dequeue),
    ("Traverse", traverse),
    ("Check Empty", check_empty),
    ("Check Full", check_full),
    ("Ascending Order", ascending),
    ("Descending Order", descending),
    ("Exit", root.destroy)
]

r = 0
c = 0

for text, cmd in buttons:
    tk.Button(
        button_frame,
        text=text,
        command=cmd,
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        bg="#1E88E5",
        fg="white"
    ).grid(row=r, column=c, padx=8, pady=8)

    c += 1
    if c == 2:
        c = 0
        r += 1

output = tk.Text(
    root,
    width=80,
    height=18,
    font=("Consolas", 11),
    bg="white"
)
output.pack(pady=15)

root.mainloop()
