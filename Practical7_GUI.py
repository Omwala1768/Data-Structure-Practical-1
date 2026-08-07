import tkinter as tk
from tkinter import scrolledtext
import heapq
from collections import Counter

# ---------------- Huffman Node ---------------- #

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ---------------- Huffman Functions ---------------- #

def build_huffman_tree(frequencies, output):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

        output.insert(tk.END,
                      f"Merging Nodes : {left.char} ({left.freq}) and {right.char} ({right.freq})\n")

    return heap[0]


def generate_codes(node, output, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix
            output.insert(tk.END,
                          f"Assign code to Character '{node.char}' : {prefix}\n")

        generate_codes(node.left, output, prefix + "0", codebook)
        generate_codes(node.right, output, prefix + "1", codebook)

    return codebook


def huffman_encoding(data, output):

    frequencies = Counter(data)

    output.insert(tk.END,
                  f"\nCharacter Frequencies : {dict(frequencies)}\n\n")

    root = build_huffman_tree(frequencies, output)

    output.insert(tk.END, "\n")

    codebook = generate_codes(root, output)

    encoded_data = ''.join(codebook[ch] for ch in data)

    output.insert(tk.END,
                  f"\nEncoded Data : {encoded_data}\n")

    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook, output):

    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    output.insert(tk.END, "\n")

    for bit in encoded_data:

        current += bit

        if current in reverse:
            output.insert(
                tk.END,
                f"Decoding : {current} -> {reverse[current]}\n"
            )

            decoded += reverse[current]
            current = ""

    return decoded


# ---------------- Button Function ---------------- #

def run_huffman():

    output.delete(1.0, tk.END)

    output.insert(tk.END, "Om Wala S119\n")
    output.insert(tk.END, "=" * 50 + "\n\n")

    data = entry.get()

    if data == "":
        output.insert(tk.END, "Please enter some text.\n")
        return

    output.insert(tk.END, "Starting Huffman Encoding...\n\n")

    encoded_data, codebook = huffman_encoding(data, output)

    output.insert(tk.END, "\nEncoding Completed!\n\n")

    output.insert(tk.END, f"Codebook : {codebook}\n\n")

    output.insert(tk.END, "Starting Huffman Decoding...\n\n")

    decoded = huffman_decoding(encoded_data, codebook, output)

    output.insert(tk.END, "\nDecoding Completed!\n\n")

    output.insert(tk.END, f"Original Data : {data}\n")
    output.insert(tk.END, f"Decoded Data  : {decoded}\n\n")

    if data == decoded:
        output.insert(tk.END,
                      "Success : Original and Decoded data match!\n")
    else:
        output.insert(tk.END,
                      "Error : Original and Decoded data do not match!\n")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Huffman Coding - Om Wala S119")
root.geometry("800x650")
root.configure(bg="#DCEEFF")

title = tk.Label(
    root,
    text="Huffman Coding GUI",
    font=("Arial", 20, "bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

frame = tk.Frame(root, bg="#DCEEFF")
frame.pack(pady=15)

label = tk.Label(
    frame,
    text="Enter Text :",
    font=("Arial", 12, "bold"),
    bg="#DCEEFF"
)
label.grid(row=0, column=0, padx=10)

entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=40
)
entry.grid(row=0, column=1)

btn = tk.Button(
    root,
    text="Encode & Decode",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    padx=15,
    command=run_huffman
)
btn.pack(pady=10)

output = scrolledtext.ScrolledText(
    root,
    width=95,
    height=28,
    font=("Consolas", 10)
)
output.pack(padx=10, pady=10)

root.mainloop()
