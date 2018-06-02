class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.iter = None

    def __iter__(self):
        self.iter = self.head
        return self

    def __next__(self):
        if self.iter is None:
            raise StopIteration
        else:
            node = self.iter
            self.iter = self.iter.next
            return node

    def __len__(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def __contains__(self, data):
        node = self.get_nodes(data)[1]

        if node is not None:
            return True
        return False

    def __str__(self):
        return self.visualize(6)

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove(self, data):
        previous, node = self.get_nodes(data)

        if previous is None:
            self.head = node.next
        else:
            previous.next = node.next

    def search(self, data):
        node = self.get_nodes(data)[1]
        if node is not None:
            return node.data
        return node

    def get_nodes(self, data):
        previous = None
        current = self.head
        found = False

        while not found and current is not None:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next

        return previous, current

    def visualize(self, max_char):
        output = "\n" + "\t "

        for _ in self:
            output += "-" * (max_char + 2) + " " * 8
        output += "\n" + "\t"

        for node in self:
            length = len(str(node.data))
            spacing = ((max_char - length) // 2)

            output += "| " + " " * spacing + node.data + \
                      " " * (max_char - length - spacing) + " |"

            output += " ---> "

        output += "\n" + "\t "
        for _ in self:
            output += "-" * (max_char + 2) + " " * 8

        return output