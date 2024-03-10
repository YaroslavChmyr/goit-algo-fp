import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title, fig):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(fig)
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_traversal(root):
    if root is None:
        return
    stack = [(root, 0)]
    visited = set()
    fig = plt.figure(figsize=(12, 8))
    color_step = 256 // (count_nodes(root) + 1)
    while stack:
        node, step = stack.pop()
        if node.id not in visited:
            color = "#%02X%02X%02X" % (0, 0, 255 - color_step * step)
            node.color = color
            visited.add(node.id)
            if node.right:
                stack.append((node.right, step + 1))
            if node.left:
                stack.append((node.left, step + 2))
    draw_tree(root, "Обхід в глибину", fig)

def breadth_first_traversal(root):
    if root is None:
        return
    queue = [(root, 0)]
    visited = set()
    fig = plt.figure(figsize=(12, 8))
    while queue:
        node, step = queue.pop(0)
        if node.id not in visited:
            color = "#%02X%02X%02X" % (0, 255 - step * 30, 0)
            node.color = color
            visited.add(node.id)
            if node.left:
                queue.append((node.left, step + 1))
            if node.right:
                queue.append((node.right, step + 2))
    draw_tree(root, "Обхід в ширину", fig)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Створення дерева
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.left = Node(9)
root.left.right.right = Node(10)

# Обходи дерева та візуалізація
depth_first_traversal(root)
breadth_first_traversal(root)