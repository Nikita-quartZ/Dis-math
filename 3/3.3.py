import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

class Tree:

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, parent, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, parent, value)

        return node, parent, False
    
    def __init__(self):
        self.root = None
    
    def plot_tree(self):
        def edges(graph, node, pos, x = 0, y = 0, level = 1, dx = 10):
            if node is not None:
                graph.add_node(node.data, pos=(x, y))
                if node.left:
                    graph.add_edge(node.data, node.left.data)
                    edges(graph, node.left, pos, x - dx / (2 ** level), y - 2, level + 1, dx)
                if node.right:
                    graph.add_edge(node.data, node.right.data)
                    edges(graph, node.right, pos, x + dx /(2 ** level), y - 2, level + 1, dx)

        di_graph = nx.DiGraph()
        position = {}
        if self.root:
            edges(di_graph, self.root, position)

        position = nx.get_node_attributes(di_graph, 'pos')

        plt.figure(figsize=(12, 8))
        nx.draw(di_graph, position, with_labels = True, node_size = 1200, node_color = "yellow",)
        plt.show()

    def balanced_tree(self, values):
        def tree(values):
            if not values:
                return None
            mid = len(values) // 2
            root = Node(values[mid])
            root.left = tree(values[:mid])
            root.right = tree(values[mid + 1:])
            return root
        self.root = tree(sorted(values))


    def wide_tree(self, node):
        if node is None:
            return
        vertex = [node]
        while vertex:
            vertex_array = []
            for node in vertex:
                if node.left:
                    vertex_array += [node.left]
                if node.right:
                    vertex_array += [node.right]
            vertex = vertex_array

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        node, parent, flag = self.__find(self.root, None, obj.data)

        if not flag and node:
            if obj.data < node.data:
                node.left = obj
            else:
                node.right = obj

        return obj

x = 23
a_0 = 1

tree = Tree()
current_value = a_0
seen_values = set()

while current_value not in seen_values:
    seen_values.add(current_value)
    current_value = (current_value * (x + 5)) % 700

tree = Tree()
tree.balanced_tree(list(seen_values))
tree.wide_tree(tree.root)
tree.plot_tree()


