import tkinter as tk
from tkinter import messagebox

stack = []
def add_text():
    text = entry.get()

    if text == "":
        messagebox.showwarning("Warning", "Enter some text.")
        return

    stack.append(text)
    entry.delete(0, tk.END)
    update_display()

def undo():
    if len(stack) == 0:
        messagebox.showinfo("Undo", "Nothing to Undo!")
    else:
        removed = stack.pop()
        messagebox.showinfo("Undo", f"Removed: {removed}")
        update_display()

def update_display():
    if len(stack) == 0:
        display.config(text="Current Text: Empty")
    else:
        display.config(text="Current Text: " + " ".join(stack))

root = tk.Tk()
root.title("Undo Mechanism")
root.geometry("450x250")
root.resizable(False, False)

tk.Label(root,
         text="Enter Text",
         font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack()

tk.Button(root,
          text="Add Text",
          font=("Arial", 12),
          width=15,
          command=add_text).pack(pady=10)

tk.Button(root,
          text="Undo",
          font=("Arial", 12),
          width=15,
          command=undo).pack()

display = tk.Label(root,
                   text="Current Text: Empty",
                   font=("Arial", 12, "bold"))
display.pack(pady=20)

root.mainloop()
