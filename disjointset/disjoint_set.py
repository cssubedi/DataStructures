class DisjointSet(object):
    def __init__(self, size):
        self.size = size
        self.array = [-1 for _ in range(self.size)]

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return self._visualize()

    def union_by_size(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        assert self.array[root1] < 0, "The node is not root."
        assert self.array[root2] < 0, "The node is not root."

        if root1 == root2:
            return

        if (- self.array[root1]) > (- self.array[root2]):
            self.array[root1] += self.array[root2]
            self.array[root2] = root1
        else:
            self.array[root2] += self.array[root1]
            self.array[root1] = root2

    def union_by_height(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        assert self.array[root1] < 0, "The node is not root."
        assert self.array[root2] < 0, "The node is not root."

        if root1 == root2:
            return

        if self.array[root2] < self.array[root1]:
            self.array[root1] = root2
        else:
            if self.array[root1] == self.array[root2]:
                self.array[root1] -= 1
            self.array[root2] = root1

    def find(self, element):
        if self.array[element] < 0:
            return element
        else:
            result = self.find(self.array[element])
            self.array[element] = result
            return result

    def _visualize(self):
        d_sets = [[] for _ in range(self.size)]
        for i in range(self.size):
            j = i
            while self.array[j] >= 0:
                j = self.array[j]
            d_sets[j].append(i)

        d_sets = [x for x in d_sets if x != []]
        return str(d_sets)
