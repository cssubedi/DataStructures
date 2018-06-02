class LinkedListNode(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class LinkedList(object):
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

    def __contains__(self, key):
        node = self.get_nodes(key)[1]

        if node is not None:
            return True
        return False

    def add(self, key, data):
        node = LinkedListNode(key, data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove(self, key):
        previous, node = self.get_nodes(key)

        if node is None:
            raise KeyError("The key {} is not found".format(key))
        elif previous is None:
            self.head = node.next
        else:
            previous.next = node.next

    def search(self, key):
        node = self.get_nodes(key)[1]
        if node is not None:
            return node.data
        return node

    def get_nodes(self, key):
        previous = None
        current = self.head
        found = False

        while not found and current is not None:
            if current.key == key:
                found = True
            else:
                previous = current
                current = current.next

        return previous, current

