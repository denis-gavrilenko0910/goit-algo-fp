import uuid
import networkx as nx
import matplotlib.pyplot as plt


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


def draw_tree(tree_root,title="Original Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.gcf().canvas.manager.set_window_title(title)  # Set window title
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal(tree_root):
    stack = [tree_root]
    visited = set()
    colors = []
    order = 0
    total_nodes = count_nodes(tree_root)
    while stack:
        node = stack.pop()
        if node is None or node.id in visited:
            continue
        visited.add(node.id)
        color_value = int(32 + (223 * order / max(1, total_nodes - 1)))  # from dark to light
        color = f'#{color_value:02X}96F0'
        colors.append((node.id, color))
        order += 1
        stack.append(node.right)
        stack.append(node.left)
    return colors


def bfs_traversal(tree_root):
    queue = [tree_root]
    visited = set()
    colors = []
    order = 0
    total_nodes = count_nodes(tree_root)
    while queue:
        node = queue.pop(0)
        if node is None or node.id in visited:
            continue
        visited.add(node.id)
        color_value = int(32 + (223 * order / max(1, total_nodes - 1)))  # from dark to light
        color = f'#{color_value:02X}96F0'
        colors.append((node.id, color))
        order += 1
        queue.append(node.left)
        queue.append(node.right)
    return colors

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def visualize_traversal(tree_root, traversal_type='dfs'):
    if traversal_type == 'dfs':
        colors = dfs_traversal(tree_root)
    elif traversal_type == 'bfs':
        colors = bfs_traversal(tree_root)
    else:
        raise ValueError("Traversal type must be 'dfs' or 'bfs'.")

    tree = nx.DiGraph() 
    pos = {tree_root.id: (0, 0)} 
    add_edges(tree, tree_root, pos) 

    for node_id, color in colors: 
        if node_id in tree.nodes:
            tree.nodes[node_id]['color'] = color 

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.gcf().canvas.manager.set_window_title(f"{traversal_type.upper()} Traversal Visualization")
    plt.title(f"{traversal_type.upper()} Traversal Visualization")
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500,  
    node_color=[tree.nodes[node]['color'] for node in tree.nodes])
    plt.tight_layout()
    plt.show() 

# Example of an unbalanced tree (to clearly see DFS vs BFS)
root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.left.left = Node(1)
root.left.right = Node(7)
root.left.right.left = Node(6)
root.right = Node(15)
root.right.right = Node(18)

# Draw original tree
print("Original tree:")
draw_tree(root)

# Visualize DFS traversal
print("DFS traversal visualization:")
visualize_traversal(root, traversal_type='dfs')

# Visualize BFS traversal
print("BFS traversal visualization:")
visualize_traversal(root, traversal_type='bfs')


