from collections import deque, defaultdict
import tkinter as tk
from tkinter import messagebox
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs_tree(self, start):
        visited = set()
        bfs_tree = defaultdict(list)
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_tree[current].append(neighbor)
                    queue.append(neighbor)

        return bfs_tree

    def display(self):
        result = ""

        for vertex, edges in self.graph.items():
            result += f"{vertex}: {edges}\n"

        return result


def create_graph():
    global graph

    graph = Graph()

    for vertex in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_vertex(vertex)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')


def run_bfs():
    start = start_entry.get().upper()

    if start not in graph.graph:
        messagebox.showerror("Error", "Enter a valid starting vertex.")
        return

    bfs_tree = graph.bfs_tree(start)

    output_text.delete("1.0", tk.END)

    output_text.insert(tk.END, "Om Wala S119\n")
    output_text.insert(tk.END, "=" * 35 + "\n\n")

    output_text.insert(tk.END, "Graph:\n")
    output_text.insert(tk.END, graph.display())

    output_text.insert(
        tk.END,
        f"\nBreadth-First Tree starting from {start}:\n"
    )

    for vertex in bfs_tree:
        output_text.insert(
            tk.END,
            f"{vertex}: {bfs_tree[vertex]}\n"
        )

    draw_graph(start, bfs_tree)


def draw_graph(start, bfs_tree):
    for widget in graph_frame.winfo_children():
        widget.destroy()

    G = nx.Graph()

    for vertex in graph.graph:
        G.add_node(vertex)

    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            G.add_edge(vertex, neighbor)

    position = {
        'A': (0, 2),
        'B': (-1, 1),
        'C': (1, 1),
        'D': (-2, 0),
        'E': (0, 0),
        'F': (2, 0)
    }

    figure = Figure(figsize=(7, 5), dpi=100)
    axis = figure.add_subplot(111)

    nx.draw(
        G,
        position,
        ax=axis,
        with_labels=True,
        node_size=1800,
        font_size=14,
        font_weight="bold"
    )

    axis.set_title(f"BFS Graph - Starting Vertex: {start}")

    figure.tight_layout()

    canvas = FigureCanvasTkAgg(
        figure,
        master=graph_frame
    )

    canvas.draw()
    canvas.get_tk_widget().pack(
        fill=tk.BOTH,
        expand=True
    )


root = tk.Tk()
root.title("BFS Graph - Om Wala S119")
root.geometry("1000x750")
root.configure(bg="#F4F6F8")

create_graph()

title_label = tk.Label(
    root,
    text="Breadth-First Search Graph",
    font=("Segoe UI", 24, "bold"),
    bg="#F4F6F8",
    fg="#333333"
)

title_label.pack(pady=(15, 5))

student_label = tk.Label(
    root,
    text="Om Wala S119",
    font=("Segoe UI", 14, "bold"),
    bg="#F4F6F8",
    fg="#4A90E2"
)

student_label.pack(pady=(0, 10))


input_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=12
)

input_frame.pack(
    fill=tk.X,
    padx=30,
    pady=5
)


start_label = tk.Label(
    input_frame,
    text="Starting Vertex:",
    font=("Segoe UI", 12, "bold"),
    bg="white"
)

start_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=8
)


start_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    width=10
)

start_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)

start_entry.insert(0, "A")


bfs_button = tk.Button(
    input_frame,
    text="Run BFS",
    font=("Segoe UI", 12, "bold"),
    bg="#4A90E2",
    fg="white",
    padx=20,
    pady=7,
    command=run_bfs
)

bfs_button.grid(
    row=0,
    column=2,
    padx=15,
    pady=8
)


output_frame = tk.Frame(
    root,
    bg="white"
)

output_frame.pack(
    fill=tk.X,
    padx=30,
    pady=10
)


output_text = tk.Text(
    output_frame,
    height=10,
    font=("Consolas", 11),
    bg="white"
)

output_text.pack(
    fill=tk.X,
    padx=10,
    pady=10
)


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
