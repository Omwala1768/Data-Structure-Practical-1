import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Operations Visualizer")
        self.root.geometry("1200x750")
        self.root.configure(bg="#0A2472")

        self.stack = Stack()

        # ================= LEFT FRAME =================

        left_frame = tk.Frame(
            root,
            bg="#FFD700",
            padx=20,
            pady=20
        )
        left_frame.pack(side="left", fill="both", expand=True)

        title = tk.Label(
            left_frame,
            text="STACK OPERATIONS",
            font=("Arial", 24, "bold"),
            bg="#FFD700",
            fg="#0A2472"
        )
        title.pack(pady=15)

        self.entry = tk.Entry(
            left_frame,
            font=("Arial", 16)
        )
        self.entry.pack(fill="x", pady=15)

        btn_frame = tk.Frame(
            left_frame,
            bg="#FFD700"
        )
        btn_frame.pack(pady=15)

        button_style = {
            "font": ("Arial", 11, "bold"),
            "width": 15,
            "height": 2,
            "bg": "#0A2472",
            "fg": "white"
        }

        tk.Button(
            btn_frame,
            text="Push",
            command=self.push_item,
            **button_style
        ).grid(row=0, column=0, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Pop",
            command=self.pop_item,
            **button_style
        ).grid(row=0, column=1, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Peek",
            command=self.peek_item,
            **button_style
        ).grid(row=1, column=0, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Is Empty?",
            command=self.check_empty,
            **button_style
        ).grid(row=1, column=1, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Size",
            command=self.stack_size,
            **button_style
        ).grid(row=2, column=0, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Exit",
            command=self.exit_program,
            font=("Arial", 11, "bold"),
            width=15,
            height=2,
            bg="red",
            fg="white"
        ).grid(row=2, column=1, padx=8, pady=8)

        tk.Label(
            left_frame,
            text="Current Stack",
            font=("Arial", 18, "bold"),
            bg="#FFD700",
            fg="#0A2472"
        ).pack(pady=15)

        self.stack_display = tk.Listbox(
            left_frame,
            height=18,
            width=35,
            font=("Arial", 14, "bold")
        )
        self.stack_display.pack(pady=10)

        self.status_label = tk.Label(
            left_frame,
            text="Welcome!",
            font=("Arial", 16, "bold"),
            bg="#FFD700",
            fg="#0A2472",
            wraplength=500
        )
        self.status_label.pack(pady=15)

        # ================= RIGHT FRAME =================

        right_frame = tk.Frame(
            root,
            bg="#0A2472",
            padx=20,
            pady=20,
            width=450
        )
        right_frame.pack(side="right", fill="both")

        tk.Label(
            right_frame,
            text="STACK THEORY",
            font=("Arial", 24, "bold"),
            bg="#0A2472",
            fg="#FFD700"
        ).pack(pady=10)

        info_text = """
STACK (LIFO) Last In First Out
The last element inserted
is the first one removed.

━━━━━━━━━━━━━━━━━━━━

OPERATIONS:
1. Push - Add an element to the top

2. Pop - Remove the top element

3. Peek - View the top element

4. Is Empty - Check whether stack has data

5. Size - Show total elements

━━━━━━━━━━━━━━━━━━━━

ADVANTAGES :
✓ Fast insertion and deletion
✓ Simple implementation
✓ Used in Undo / Redo
✓ Useful in Recursion

━━━━━━━━━━━━━━━━━━━━

DISADVANTAGES :
✗ Only top element accessible
✗ No random access
✗ Searching is inefficient
"""

        text_widget = tk.Text(
            right_frame,
            wrap="word",
            font=("Arial", 14),
            bg="#FFF8DC",
            fg="black",
            padx=20,
            pady=20
        )

        text_widget.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        text_widget.insert("1.0", info_text)
        text_widget.config(state="disabled")

    # ================= FUNCTIONS =================

    def update_display(self):
        self.stack_display.delete(0, tk.END)

        for item in reversed(self.stack.items):
            self.stack_display.insert(tk.END, item)

    def push_item(self):
        item = self.entry.get().strip()

        if item == "":
            messagebox.showwarning(
                "Input Error",
                "Please enter an element."
            )
            return

        self.stack.push(item)
        self.update_display()

        self.status_label.config(
            text=f"'{item}' pushed successfully."
        )

        messagebox.showinfo(
            "Push Operation",
            f"'{item}' has been pushed onto the stack."
        )

        self.entry.delete(0, tk.END)

    def pop_item(self):
        try:
            item = self.stack.pop()

            self.update_display()

            self.status_label.config(
                text=f"'{item}' popped successfully."
            )

            messagebox.showinfo(
                "Pop Operation",
                f"'{item}' has been popped from the stack."
            )

        except IndexError:
            messagebox.showerror(
                "Error",
                "Stack is Empty"
            )

    def peek_item(self):
        try:
            item = self.stack.peek()

            self.status_label.config(
                text=f"Top Element : {item}"
            )

            messagebox.showinfo(
                "Peek Operation",
                f"Top Element is: {item}"
            )

        except IndexError:
            messagebox.showerror(
                "Error",
                "Stack is Empty"
            )

    def check_empty(self):
        result = self.stack.is_empty()

        self.status_label.config(
            text=f"Stack Empty ? {'Yes' if result else 'No'}"
        )

        messagebox.showinfo(
            "Is Empty",
            f"Stack Empty? {'Yes' if result else 'No'}"
        )

    def stack_size(self):
        size = self.stack.size()

        self.status_label.config(
            text=f"Stack Size : {size}"
        )

        messagebox.showinfo(
            "Stack Size",
            f"Number of elements in stack: {size}"
        )

    def exit_program(self):
        answer = messagebox.askyesno(
            "Exit Program",
            "Are you sure you want to exit?"
        )

        if answer:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
