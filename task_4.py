import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Extra argument to store node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Using id and storing node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value as label

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)
    return node

# Example usage:
heap = [10, 7, 10, 5, 1, 10, 3]  # Example heap array3
# Build heap tree from the heap array
heapq.heapify(heap)  # Ensure the heap property is maintained
heap_tree_root = build_heap_tree(heap)
# Display the heap tree
draw_tree(heap_tree_root)
# The code builds a binary tree from a heap array and visualizes it using NetworkX and Matplotlib.
print(heap)


