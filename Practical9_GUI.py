import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def linear_probing_insert(hash_size, data):
    hash_table = [None] * hash_size

    for value in data:
        hash_index = value % hash_size
        original_index = hash_index

        while hash_table[hash_index] is not None:
            hash_index = (hash_index + 1) % hash_size

            if hash_index == original_index:
                messagebox.showerror("Error", "Hash table is full!")
                return hash_table

        hash_table[hash_index] = value

    return hash_table


def generate_table():
    try:
        hash_size = int(size_entry.get())

        if hash_size <= 0:
            messagebox.showerror("Error", "Enter a valid hash table size.")
            return

        data_input = data_entry.get()

        if not data_input:
            messagebox.showerror("Error", "Enter some data.")
            return

        data = list(map(int, data_input.split()))

        final_table = linear_probing_insert(hash_size, data)

        output_text.delete("1.0", tk.END)

        output_text.insert(tk.END, "Final Hash Table\n")
        output_text.insert(tk.END, "-" * 30 + "\n")

        for i, v in enumerate(final_table):
            output_text.insert(tk.END, f"Index {i}: {v}\n")

        for widget in graph_frame.winfo_children():
            widget.destroy()

        indices = list(range(hash_size))
        values = [0 if v is None else v for v in final_table]

        figure = Figure(figsize=(8, 4.5), dpi=100)
        axis = figure.add_subplot(111)

        axis.bar(indices, values)

        axis.set_title("Linear Probing Hash Table")
        axis.set_xlabel("Hash Table Index")
        axis.set_ylabel("Stored Value")

        axis.set_xticks(indices)
        axis.grid(axis="y", linestyle="--", alpha=0.5)

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(figure, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter only numbers separated by spaces."
        )

root = tk.Tk()
root.title("Linear Probing Hash Table - Om Wala S119")
root.geometry("1000x750")
root.configure(bg="#F4F6F8")

title_label = tk.Label(
    root,
    text="Linear Probing Hash Table",
    font=("Segoe UI", 24, "bold"),
    bg="#F4F6F8",
    fg="#333333"
)
title_label.pack(pady=(20, 5))

student_label = tk.Label(
    root,
    text="Om Wala S119",
    font=("Segoe UI", 14, "bold"),
    bg="#F4F6F8",
    fg="#4A90E2"
)
student_label.pack(pady=(0, 15))

input_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=15
)
input_frame.pack(fill=tk.X, padx=30, pady=5)

size_label = tk.Label(
    input_frame,
    text="Hash Table Size:",
    font=("Segoe UI", 12, "bold"),
    bg="white"
)
size_label.grid(row=0, column=0, padx=10, pady=8)

size_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    width=15
)
size_entry.grid(row=0, column=1, padx=10, pady=8)

data_label = tk.Label(
    input_frame,
    text="Enter Data:",
    font=("Segoe UI", 12, "bold"),
    bg="white"
)
data_label.grid(row=1, column=0, padx=10, pady=8)

data_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    width=50
)
data_entry.grid(row=1, column=1, padx=10, pady=8)

generate_button = tk.Button(
    input_frame,
    text="Generate Hash Table",
    font=("Segoe UI", 12, "bold"),
    bg="#4A90E2",
    fg="white",
    padx=15,
    pady=8,
    command=generate_table
)
generate_button.grid(row=2, column=0, columnspan=2, pady=12)

output_frame = tk.Frame(
    root,
    bg="white"
)
output_frame.pack(fill=tk.X, padx=30, pady=10)

output_text = tk.Text(
    output_frame,
    height=8,
    font=("Consolas", 12),
    bg="white"
)
output_text.pack(fill=tk.X, padx=10, pady=10)

graph_frame = tk.Frame(
    root,
    bg="white"
)
graph_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=30,
    pady=(0, 20)
)


root.mainloop()
