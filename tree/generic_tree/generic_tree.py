import sys
sys.path.append("../../")
from stack.stack import Stack
from queue.queue import Queue


class Node(object):
    def __init__(self, element, first_child=None, next_sibling=None):
        self.element = element
        self.first_child = first_child
        self.next_sibling = next_sibling

    def __eq__(self, other):
        try:
            return self.element == other.element
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_children(self):
        children = []
        child = self.first_child

        if child is None:
            return None

        while child is not None:
            children.append(child)
            child = child.next_sibling

        return children


class MovingRootError(Exception): pass


class ElementNotFoundError(Exception): pass


class GenericTree(object):
    def __init__(self):
        self.root = None

    @property
    def height(self):
        if self.root is None:
            return 0
        return self._get_height(self.root)

    def add_subtree(self, parent, children):
        if self.root is None:
            parent_node = Node(parent)
            self.root = parent_node
        else:
            parent_node = self._get_node(parent)

        if not parent_node:
            raise ElementNotFoundError("Could not find parent {}".format(parent))

        children_nodes = [Node(child) for child in children]

        if children:
            if not parent_node.first_child:
                parent_node.first_child = children_nodes[0]

            else:
                sibling = parent_node.first_child
                while sibling.next_sibling:
                    sibling = sibling.next_sibling

                sibling.next_sibling = children_nodes[0]

            for i in range(len(children) - 1):
                children_nodes[i].next_sibling = children_nodes[i + 1]

    def dfs(self, current):
        # Implementation: Recursive 1
        if current is None:
            return
        next = current.first_child

        while next is not None:
            self.dfs(next)
            next = next.next_sibling

        # Implementation: Iterative 1
        # if current is None:
        #     return
        # stack = Stack()
        # stack.push(current)
        #
        # while stack:
        #     current = stack.top_pop()
        #
        #     if current.next_sibling is not None:
        #         stack.push(current.next_sibling)
        #     if current.first_child is not None:
        #         stack.push(current.first_child)

        # Implementation: Iterative 2
        # if current is None:
        #     return
        # stack = Stack()
        # stack.push(current)
        #
        # while stack:
        #     current = stack.top_pop()
        #     children = current.get_children()
        #
        #     if children:
        #         for child in children:
        #             stack.push(child)

    def bfs(self, current):
        # Implementation: Iterative 1
        if current is None:
            return
        queue = Queue()
        queue.enqueue(current)

        while current is not None:
            current = current.next_sibling

            if queue and current is None:
                current = queue.dequeue().first_child

            if current and current.first_child:
                queue.enqueue(current)

        # Implementation: Iterative 2
        # if current is None:
        #     return
        # queue = Queue()
        # queue.enqueue(current)
        #
        # while queue:
        #     current = queue.dequeue()
        #     children = current.get_children()
        #
        #     if children:
        #         for child in children:
        #             queue.enqueue(child)

    def move(self, element, parent):
        moving_node = self._get_node(element)
        destination_node = self._get_node(parent)

        if not moving_node:
            raise ElementNotFoundError("Could not find element {}".format(element))

        if not destination_node:
            raise ElementNotFoundError("Could not find parent {}".format(parent))

        if moving_node == self.root:
            raise MovingRootError("Cannot move root node.")

        parent_node = None
        previous_sibling_node = None

        queue = Queue()
        queue.enqueue(self.root)

        while queue:
            current = queue.dequeue()

            if current.first_child == moving_node:
                parent_node = current
            if current.next_sibling == moving_node:
                previous_sibling_node = current

            if current == moving_node:
                break

            children = current.get_children()
            if children:
                for child in children:
                    queue.enqueue(child)

        if parent_node:
            parent_node.first_child = moving_node.next_sibling

        if previous_sibling_node:
            previous_sibling_node.next_sibling = moving_node.next_sibling

        next_sibling_node = destination_node.first_child
        destination_node.first_child = moving_node
        moving_node.next_sibling = next_sibling_node

    def _get_height(self, root):
        """
        A recursive linear time algorithm to obtain height of the tree.

        """
        if root.get_children() is None:
            return 0
        return max(
            self._get_height(node) for node in root.get_children()) + 1

    def _get_node(self, element):
        queue = Queue()
        queue.enqueue(self.root)

        while queue:
            current = queue.dequeue()
            if current.element == element:
                return current

            children = current.get_children()

            if children:
                for child in children:
                    queue.enqueue(child)
        return None

    def __str__(self):
        node = self.root
        if node is not None:
            return "    " + self._visualize(node)[5:]
        else:
            return ""

    def _visualize(self, node, layer=0):
        result = "    |" * (layer) + "\n" + \
                 "    |" * (layer) + "--->" + "[ {} ]".format(node.element) + \
                 "\n"

        children = node.get_children()
        if children:
            for child in children:
                result += self._visualize(child, layer + 1)

        return result



