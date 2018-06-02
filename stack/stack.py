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
