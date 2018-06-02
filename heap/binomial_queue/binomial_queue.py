class BinomialTree(object):
    def __init__(self, root):
        self.rank = 0
        self.root = root
        self.children = []

    def __str__(self):
        return self._visualize()

    def link(self, other_tree):
        assert self.rank == other_tree.rank, "Unequal rank."
        assert self.root <= other_tree.root, "Min root property violated."

        self.children.append(other_tree)
        self.rank += 1

    def _get_indices(self):
        indices = []
        if self.rank == 0:
            return indices
        elif self.rank == 1:
            indices.append(0)
            return indices
        else:
            indices = [0]
            for i in range(2, self.rank+1):
                indices.append(2**(i-2))
            return indices

    def _visualize(self, max_char=2, spacing=2):
        result = ""
        if self.rank == 0:
            max_width = max_char + spacing
        else:
            max_width = (max_char + spacing)*2**(self.rank-1)

        nodes = [self]
        layer = 0
        indices = [0]

        while layer <= self.rank:
            str_data = " "*max_width
            str_underscore = " "*max_width

            if layer > 0:
                str_bar = " "*max_width
                for index in indices:
                    str_bar = str_bar[: index] + \
                        str_bar[index: index+1].replace(" ", "|") + \
                        str_bar[index+1:]

                result += "\n" + str_bar

            for i in range(len(indices)):
                index = indices[i]
                node = nodes[i]

                str_data = str_data[:index] + \
                    str_data[index:index+1].replace(" ", str(node.root)) + \
                    str_data[index+1:]
                if node.rank > 1:
                    end_index = index + (max_char+spacing)*2**(node.rank-2)
                    str_underscore = str_underscore[:index] + \
                        str_underscore[index:index+1].replace(" ", "|") + \
                        str_underscore[index+1:end_index].replace(" ", "_") + \
                        str_underscore[end_index:]
                elif node.rank == 1:
                    str_underscore = str_underscore[:index] + \
                        str_underscore[index:index + 1].replace(" ", "|") + \
                        str_underscore[index+1:]

            result += "\n" + str_data + "\n" + str_underscore

            count_elements = len(indices)
            for i in range(count_elements):
                node = nodes[0]
                nodes += node.children

                new_indices = [(max_char + spacing)*x for x in node._get_indices()]
                if len(new_indices) != 0:
                    indices += [indices[0] + x for x in new_indices]

                nodes.pop(0)
                indices.pop(0)

            layer += 1
        return result


class BinomialQueue(object):
    def __init__(self):
        self.trees = []
        self._elements = 0
        self.min = None
        self.min_rank = -1

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, value):
        self._elements = value
        while self._elements > (2**len(self.trees) - 1):
            self.trees.append(None)

    def __iadd__(self, other):
        """
        Complexity of merging two BQ of O(N):
            O(number of trees) = O(logN)

        """
        if type(other) == type(self):
            self.merge(other)
            return self

    def insert(self, element):
        """
        Complexity of insertion:
            Linkage = O(logN)
            CarryOver = logN-1 = O(logN)

            Total Complexity = O(logN)

        """
        tree = BinomialTree(element)
        self.elements = self.elements + 2 ** tree.rank
        self.add_tree(tree)

    def delete_min(self):
        """
        Complexity of deleting min from BQ
            Merge generated BQ = O(logN)
            Find new min = O(logN)

            Total Complexity = O(logN)

        """
        if len(self.trees) == 0:
            return
        min_tree = self.trees[self.min_rank]
        self.trees[self.min_rank] = None
        self.elements = self.elements - 2 ** min_tree.rank

        for tree in min_tree.children:
            self.elements = self.elements + 2 ** tree.rank
            self.add_tree(tree)

        self.min = None
        self.min_rank = -1

        for tree in self.trees:
            if tree is not None:
                self.update_min(tree)

    def __str__(self):
        result = ""
        for tree in self.trees:
            if tree:
                result += str(tree)
            else:
                result += "\n" + str(tree) + "\n"
        return result

    def update_min(self, tree):
        if self.min is None:
            self.min = tree.root
            self.min_rank = tree.rank

        elif tree.root <= self.min:
            self.min = tree.root
            self.min_rank = tree.rank

    def add_tree(self, new_tree):
        rank = new_tree.rank
        if self.trees[rank] is None:
            self.trees[rank] = new_tree
            self.update_min(new_tree)
            return

        if self.trees[rank].root < new_tree.root:
            new_tree, self.trees[rank] = self.trees[rank], new_tree

        new_tree.link(self.trees[rank])
        self.trees[rank] = None
        self.add_tree(new_tree)

    def merge(self, other_queue):
        self.elements = self.elements + other_queue.elements
        for tree in other_queue.trees:
            if tree is not None:
                self.add_tree(tree)
