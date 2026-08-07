import tkinter as tk
from tkinter import scrolledtext
import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, output):
        self.output = output

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        self.output.insert(tk.END, f"Left Rotation on {z.key}\n")

        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        self.output.insert(tk.END, f"Right Rotation on {z.key}\n")

        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def pre_order(self, root):
        if root:
            self.output.insert(tk.END, str(root.key) + " ")
            self.pre_order(root.left)
            self.pre_order(root.right)

def min_heap_example(data, output):
    heapq.heapify(data)
    output.insert(tk.END, f"Min-Heap : {data}\n")

def max_heap_example(data, output):
    max_heap = [-i for i in data]
    heapq.heapify(max_heap)
    output.insert(tk.END, f"Max-Heap : {[-i for i in max_heap]}\n")

class TaskManager:
    def __init__(self, output):
        self.pq = []
        self.output = output

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def run_tasks(self):
        self.output.insert(tk.END, "\nProcessing Tasks by Priority:\n")
        while self.pq:
            priority, task = heapq.heappop(self.pq)
            self.output.insert(tk.END, f"Priority {priority} -> Task: {task}\n")

def run_program():
    output.delete(1.0, tk.END)

    output.insert(tk.END, "Om Wala S119\n")
    output.insert(tk.END, "=" * 60 + "\n\n")

    output.insert(tk.END, "=== AVL Tree Insertion and Balancing ===\n\n")

    avl = AVLTree(output)
    root = None

    avl_inputs = [20, 4, 15, 70, 50, 100, 80]

    for value in avl_inputs:
        output.insert(tk.END, f"Inserting {value}...\n")
        root = avl.insert(root, value)

    output.insert(tk.END, "\nAVL Tree Pre-Order Traversal:\n")
    avl.pre_order(root)

    output.insert(tk.END, "\n\n=== Heap Examples ===\n")

    data = [9, 5, 6, 2, 3]

    min_heap_example(data.copy(), output)
    max_heap_example(data.copy(), output)

    output.insert(tk.END, "\n\n=== Task Manager using Priority Queue ===\n")

    manager = TaskManager(output)

    manager.add_task(2, "Low priority: Backup database")
    manager.add_task(1, "High priority: Handle emergency patient")
    manager.add_task(3, "Medium priority: Run diagnostics")

    manager.run_tasks()

root = tk.Tk()
root.title("AVL Tree and Heap - Om Wala S119")
root.geometry("850x650")
root.configure(bg="#DCEEFF")

title = tk.Label(
    root,
    text="AVL Tree and Heap GUI",
    font=("Arial", 20, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

button = tk.Button(
    root,
    text="Run Program",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    command=run_program
)
button.pack(pady=15)

output = scrolledtext.ScrolledText(
    root,
    width=100,
    height=32,
    font=("Consolas", 10)
)
output.pack(padx=10, pady=10)

root.mainloop()
