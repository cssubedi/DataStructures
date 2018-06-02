from undirected_graph_data_structures import Node, LinkedList


class Vertex(object):
    def __init__(self, element):
        self.element = element
        self.visited = False
        self.parents = LinkedList()
        self.children = LinkedList()
        self.interval = []

    @property
    def out_degree(self):
        return len(self.children)

    @property
    def in_degree(self):
        return len(self.parents)

    @property
    def edges(self):
        return self.children


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1]

    def top_pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)