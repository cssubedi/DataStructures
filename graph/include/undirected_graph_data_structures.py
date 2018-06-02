class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self.__eq__(other)


class Vertex(object):
    def __init__(self, element):
        self.element = element
        self.edges = LinkedList()
        self.visited = False
        self.distance = None
        self.interval = []

    def __eq__(self, other):
        return self.element == other.element

    def __ne__(self, other):
        return not self.__eq__(other)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def __contains__(self, item):
        node = self.get_node(item)

        if node is not None:
            return True
        else:
            return False

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def remove(self, element):
        node = self.get_node(element)

        if len(self) == 1:
            self.head = None
        elif node.previous is None:     # If the head element is removed
            node.next.previous = None
            self.head = node.next
        elif node.next is None:         # If the tail element is removed
            node.previous.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def get_node(self, element):
        current = self.head
        found = False

        while current is not None and not found:
            if element == current.data.element:
                found = True
            else:
                current = current.next

        return current

    def reset_head(self, element):
        node = self.get_node(element)
        if node != self.head:
            node.previous.next = None
            self.tail.next = self.head
            self.head.previous = self.tail
            self.head = node
            self.tail = node.previous
            node.previous = None


class LinkedListIterator(object):
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            result = self.current
            self.current = self.current.next

            return result
