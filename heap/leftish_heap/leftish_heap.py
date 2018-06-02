class LeftishHeapNode(object):
    def __init__(self, data, right_child=None, left_child=None, npl=0):
        self.data = data
        self.right_child = right_child
        self.left_child = left_child
        self.npl = npl

    def __le__(self, other):
        return self.data <= other.data

    def swap_children(self):
        self.right_child, self.left_child = self.left_child, self.right_child

    def merge(self, other_root):
        if other_root is None:
            return self
        if self.data <= other_root.data:
            return self.recur_merge(other_root)
        else:
            return other_root.recur_merge(self)

    def recur_merge(self, other_root):
        if self.left_child is None:
            self.left_child = other_root
        else:
            if self.right_child is None:
                self.right_child = other_root
            else:
                self.right_child = self.right_child.merge(other_root)

            if self.left_child.npl < self.right_child.npl:
                self.swap_children()

            self.npl = self.right_child.npl + 1

        return self


class LeftishHeap(object):
    def __init__(self, root=None):
        self.root = root

    def __iadd__(self, other):
        """
        Complexity of merge
            O(# of nodes in the right path) = O(logN)

        """
        if type(self) == type(other):
            self.root.merge(other.root)
            if self.root <= other.root:
                return self
            else:
                return other

    def __str__(self):
        if self.root is None:
            return ""
        else:
            return self._visualize()

    @property
    def height(self):
        return self._get_height(self.root)

    def insert(self, element):
        heap_node = LeftishHeapNode(element)
        if self.root is None:
            self.root = heap_node
            return
        else:
            if self.root.data > heap_node.data:
                self.root, heap_node = heap_node, self.root
            self.root.merge(heap_node)

    def _get_indices(self, layer, max_width):
        num_indices = 2**layer
        list_indices = [None]*num_indices
        list_indices[0] = max_width//(2*num_indices)

        for i in range(1, num_indices):
            list_indices[i] = list_indices[0]*(1 + 2*i)

        return list_indices

    def _get_height(self, node):
        if node is None:
            return -1
        else:
            return max(self._get_height(node.left_child),
                       self._get_height(node.right_child)) + 1

    def _visualize(self, max_char=2):      # max_char in the payload.
        height = self.height
        result = ""
        layer = 0
        max_width = 2**(height + max_char)

        nodes = [self.root]
        while layer <= height:
            str_data = " " * max_width
            indices = self._get_indices(layer, max_width)
            len_indices = len(indices)

            if len_indices > 1:
                str_underscore = " " * max_width
                str_bar = " " * max_width
                for i in range(len_indices // 2):
                    start = indices[2 * i]
                    end = indices[2 * i + 1]
                    str_underscore = str_underscore[:start + 1] + \
                            str_underscore[start + 1:end].replace(" ", "_") + \
                            str_underscore[end:]

                    str_bar = str_bar[:start] + \
                            str_bar[start:start + 1].replace(" ", "|") + \
                            str_bar[start + 1:end] + \
                            str_bar[end:end + 1].replace(" ", "|") + \
                            str_bar[end + 1:]

                result += str_underscore + "\n" + str_bar + "\n"

            for i in range(len_indices):
                if nodes[i] is not None:
                    index = indices[i]
                    str_data = str_data[:index] + \
                           str_data[index:index + 1].replace(" ", str(nodes[i].data)) + \
                           str_data[index + 1:]

            count_nodes = len(nodes)
            for i in range(count_nodes):
                node = nodes[0]
                if node is not None:
                    nodes.append(node.left_child)
                    nodes.append(node.right_child)
                else:
                    nodes.append(None)
                    nodes.append(None)
                nodes.pop(0)

            layer += 1
            result += str_data + "\n"

        return result

