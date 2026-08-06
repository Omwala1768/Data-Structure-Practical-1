import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue is Full, Cannot Enqueue Item"
        self.queue.append(item)
        return f"Enqueued Item {item} in Queue"

    def dequeue(self):
        if self.is_empty():
            return "Cannot Dequeue Item, Queue is Empty"
        item = self.queue.pop(0)
        return f"Dequeued Item {item} from Queue"

    def front(self):
        if self.is_empty():
            return "Queue is Empty"
        return f"Front of the Queue is {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is Empty"
        return "Queue Contains: " + " ".join(map(str, self.queue))

    def display_queue(self):
        if self.is_empty():
            return "Queue is Empty"
        text = "Displaying Queue:\n"
        for i, item in enumerate(self.queue):
            text += f"{i+1}. {item}\n"
        return text

q = None

def create_queue():
    global q
    try:
        size = int(size_entry.get())
        if size <= 0:
            raise ValueError
        q = Queue(size)
        output.delete(1.0, tk.END)
        output.insert(tk.END, f"Queue Created Successfully\nMaximum Size = {size}")
    except:
        messagebox.showerror("Error", "Enter a Valid Queue Size")

def enqueue():
    global q
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    try:
        item = int(item_entry.get())
        result = q.enqueue(item)
        output.delete(1.0, tk.END)
        output.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Enter a Valid Integer")

def dequeue():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    output.insert(tk.END, q.dequeue())

def front():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    output.insert(tk.END, q.front())

def traverse():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    output.insert(tk.END, q.traverse())

def display():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    output.insert(tk.END, q.display_queue())

def check_full():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    if q.is_full():
        output.insert(tk.END, "Queue is Full")
    else:
        output.insert(tk.END, "Queue is Not Full")

def check_empty():
    if q is None:
        messagebox.showwarning("Warning", "Create Queue First")
        return
    output.delete(1.0, tk.END)
    if q.is_empty():
        output.insert(tk.END, "Queue is Empty")
    else:
        output.insert(tk.END, "Queue is Not Empty")

root = tk.Tk()
root.title("Om Wala S119 - Queue Operations")
root.geometry("700x650")
root.configure(bg="#E8F4FC")

title = tk.Label(root, text="Om Wala S119\nQueue Operations Using Tkinter",
                 font=("Arial", 18, "bold"),
                 bg="#1976D2", fg="white", pady=10)
title.pack(fill="x")

frame = tk.Frame(root, bg="#E8F4FC")
frame.pack(pady=15)

tk.Label(frame, text="Queue Size", font=("Arial", 12, "bold"),
         bg="#E8F4FC").grid(row=0, column=0, padx=10, pady=10)

size_entry = tk.Entry(frame, font=("Arial", 12), width=15)
size_entry.grid(row=0, column=1)

tk.Button(frame, text="Create Queue", font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white", width=15,
          command=create_queue).grid(row=0, column=2, padx=10)

tk.Label(frame, text="Queue Item", font=("Arial", 12, "bold"),
         bg="#E8F4FC").grid(row=1, column=0, padx=10, pady=10)

item_entry = tk.Entry(frame, font=("Arial", 12), width=15)
item_entry.grid(row=1, column=1)

button_frame = tk.Frame(root, bg="#E8F4FC")
button_frame.pack(pady=10)

buttons = [
    ("Enqueue", enqueue),
    ("Dequeue", dequeue),
    ("Front", front),
    ("Traverse", traverse),
    ("Display Queue", display),
    ("Check Full", check_full),
    ("Check Empty", check_empty),
    ("Exit", root.destroy)
]

r = 0
c = 0

for text, cmd in buttons:
    tk.Button(button_frame,
              text=text,
              width=18,
              height=2,
              font=("Arial", 11, "bold"),
              bg="#2196F3",
              fg="white",
              command=cmd).grid(row=r, column=c, padx=8, pady=8)
    c += 1
    if c == 2:
        c = 0
        r += 1

output = tk.Text(root, width=70, height=15,
                 font=("Consolas", 11),
                 bg="white")
output.pack(pady=15)

root.mainloop()
