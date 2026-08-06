import tkinter as tk
from tkinter import messagebox

def check_delimiters():
    expression = entry.get()
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    balanced = True

    for ch in expression:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":
            if len(stack) == 0:
                balanced = False
                break

            top = stack.pop()

            if top != pairs[ch]:
                balanced = False
                break

    if len(stack) != 0:
        balanced = False

    if balanced:
        result.config(text="Balanced", fg="green")
        messagebox.showinfo("Result", "Delimiters are Balanced.")
    else:
        result.config(text="Not Balanced", fg="red")
        messagebox.showerror("Result", "Delimiters are NOT Balanced.")

root = tk.Tk()
root.title("Delimiter Matching")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="Enter Expression", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack()

tk.Button(root,
          text="Check",
          font=("Arial", 12),
          command=check_delimiters).pack(pady=15)

result = tk.Label(root, text="", font=("Arial", 14, "bold"))
result.pack()

root.mainloop()
