import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
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

    def dfs_tree(self, start):
        visited = set()
        dfs_tree = defaultdict(list)

        def dfs(vertex):
            visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_tree[vertex].append(neighbor)
                    dfs(neighbor)

        dfs(start)
        return dfs_tree

    def display(self):
        result = ""

        for vertex, edges in self.graph.items():
            result += f"{vertex}: {edges}\n"

        return result


def create_graph():
    global graph

    vertices_input = vertex_entry.get().strip()
    edges_input = edge_entry.get().strip()

    if not vertices_input:
        messagebox.showerror("Error", "Please enter vertices.")
        return

    graph = Graph()

    vertices = vertices_input.split()

    for vertex in vertices:
        graph.add_vertex(vertex.upper())

    if edges_input:
        edges = edges_input.split(",")

        for edge in edges:
            parts = edge.strip().split()

            if len(parts) != 2:
                messagebox.showerror(
                    "Error",
                    "Enter edges in the format: A-B, B-C, C-D"
                )
                return

            vertex1 = parts[0].upper()
            vertex2 = parts[1].upper()

            if vertex1 not in graph.graph or vertex2 not in graph.graph:
                messagebox.showerror(
                    "Error",
                    f"Vertex {vertex1} or {vertex2} does not exist."
                )
                return

            graph.add_edge(vertex1, vertex2)

    output_text.delete("1.0", tk.END)

    output_text.insert(tk.END, "Om Wala S119\n")
    output_text.insert(tk.END, "=" * 40 + "\n\n")
    output_text.insert(tk.END, "Graph Created Successfully!\n\n")
    output_text.insert(tk.END, "Graph:\n")
    output_text.insert(tk.END, graph.display())

    start_entry.delete(0, tk.END)

    draw_original_graph()


def run_dfs():
    if not graph.graph:
        messagebox.showerror(
            "Error",
            "Please create the graph first."
        )
        return

    start = start_entry.get().strip().upper()

    if not start:
        messagebox.showerror(
            "Error",
            "Please enter a starting vertex."
        )
        return

    if start not in graph.graph:
        messagebox.showerror(
            "Error",
            f"Vertex {start} does not exist."
        )
        return

    dfs_tree = graph.dfs_tree(start)

    output_text.delete("1.0", tk.END)

    output_text.insert(tk.END, "Om Wala S119\n")
    output_text.insert(tk.END, "=" * 40 + "\n\n")

    output_text.insert(tk.END, "Graph:\n")
    output_text.insert(tk.END, graph.display())

    output_text.insert(
        tk.END,
        f"\nDFS Tree starting from {start}:\n"
    )

    for vertex in dfs_tree:
        if dfs_tree[vertex]:
            output_text.insert(
                tk.END,
                f"{vertex}: {dfs_tree[vertex]}\n"
            )

    draw_graph(start, dfs_tree)


def draw_original_graph():
    for widget in graph_frame.winfo_children():
        widget.destroy()

    G = nx.Graph()

    for vertex in graph.graph:
        G.add_node(vertex)

    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            G.add_edge(vertex, neighbor)

    figure = Figure(figsize=(8, 4.5), dpi=100)
    axis = figure.add_subplot(111)

    position = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        position,
        ax=axis,
        with_labels=True,
        node_size=1500,
        font_size=12,
        font_weight="bold"
    )

    axis.set_title("Original Graph")

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


def draw_graph(start, dfs_tree):
    for widget in graph_frame.winfo_children():
        widget.destroy()

    G = nx.Graph()

    for vertex in graph.graph:
        G.add_node(vertex)

    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            G.add_edge(vertex, neighbor)

    T = nx.DiGraph()

    for vertex in dfs_tree:
        for neighbor in dfs_tree[vertex]:
            T.add_edge(vertex, neighbor)

    figure = Figure(figsize=(10, 5), dpi=100)

    graph_axis = figure.add_subplot(121)
    tree_axis = figure.add_subplot(122)

    position = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        position,
        ax=graph_axis,
        with_labels=True,
        node_size=1400,
        font_size=11,
        font_weight="bold"
    )

    graph_axis.set_title("Original Graph")

    tree_position = nx.spring_layout(T, seed=42)

    nx.draw(
        T,
        tree_position,
        ax=tree_axis,
        with_labels=True,
        node_size=1400,
        font_size=11,
        font_weight="bold",
        arrows=True
    )

    tree_axis.set_title("DFS Tree")

    figure.suptitle(
        f"DFS Visualization - Starting Vertex: {start}"
    )

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


graph = Graph()

root = tk.Tk()
root.title("DFS Graph - Om Wala S119")
root.geometry("1100x800")
root.configure(bg="#F4F6F8")


title_label = tk.Label(
    root,
    text="Depth-First Search Graph",
    font=("Segoe UI", 24, "bold"),
    bg="#F4F6F8",
    fg="#333333"
)

title_label.pack(pady=(15, 3))


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


vertex_label = tk.Label(
    input_frame,
    text="Vertices:",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)

vertex_label.grid(
    row=0,
    column=0,
    padx=8,
    pady=8
)


vertex_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    width=40
)

vertex_entry.grid(
    row=0,
    column=1,
    padx=8,
    pady=8
)


edge_label = tk.Label(
    input_frame,
    text="Edges:",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)

edge_label.grid(
    row=1,
    column=0,
    padx=8,
    pady=8
)


edge_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    width=40
)

edge_entry.grid(
    row=1,
    column=1,
    padx=8,
    pady=8
)


create_button = tk.Button(
    input_frame,
    text="Create Graph",
    font=("Segoe UI", 11, "bold"),
    bg="#4A90E2",
    fg="white",
    padx=15,
    pady=6,
    command=create_graph
)

create_button.grid(
    row=0,
    column=2,
    rowspan=2,
    padx=15
)


start_label = tk.Label(
    input_frame,
    text="Starting Vertex:",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)

start_label.grid(
    row=2,
    column=0,
    padx=8,
    pady=8
)


start_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    width=15
)

start_entry.grid(
    row=2,
    column=1,
    sticky="w",
    padx=8,
    pady=8
)


dfs_button = tk.Button(
    input_frame,
    text="Run DFS",
    font=("Segoe UI", 11, "bold"),
    bg="#50C878",
    fg="white",
    padx=25,
    pady=6,
    command=run_dfs
)

dfs_button.grid(
    row=2,
    column=2,
    padx=15
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
    height=9,
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
