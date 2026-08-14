from collections import deque, defaultdict
import matplotlib.pyplot as plt
import networkx as nx


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
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


def print_bfs_tree(bfs_tree, start):
    print(f"Breadth-First Tree starting from {start}:")

    for vertex in bfs_tree:
        print(f"{vertex}: {bfs_tree[vertex]}")


def plot_graph(graph, bfs_tree):
    G = nx.Graph()

    for vertex in graph.graph:
        G.add_node(vertex)

    for vertex in graph.graph:
        for neighbor in graph.graph[vertex]:
            G.add_edge(vertex, neighbor)

    position = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        position,
        with_labels=True,
        node_size=2000,
        font_size=14,
        font_weight="bold"
    )

    plt.title("BFS Graph - Om Wala S119")
    plt.show()


if __name__ == "__main__":

    print("Om Wala S119")
    print("=" * 30)

    g = Graph()

    for v in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.add_vertex(v)

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("\nGraph:")
    g.display()

    start_vertex = 'A'
    bfs_tree = g.bfs_tree(start_vertex)

    print()
    print_bfs_tree(bfs_tree, start_vertex)

    plot_graph(g, bfs_tree)
