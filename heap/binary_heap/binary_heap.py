import math as m


class BinaryHeap(object):
    def __init__(self):
        """
            The class implements a variant of binary heap called min heap.
            First element is the smallest element.

            Space Complexity = O(N)
        """
        self.array = [None]     # Initiated with a sentinel marker None.
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return ""
        else:
            return self._visualize()

    def _height(self):
        return int(m.log(self.size, 2))

    def insert(self, item):
        """
        Complexity of insertion:
            Append = O(1)
            Bubble up = O(height) = O(logN)

            Total complexity = O(logN)

        """
        self.array.append(item)
        self.size += 1
        self._bubble_up(self.size)

    def delete_min(self):
        """
        Complexity of deleting min value:
            Shifting + Reducing size = O(1)
            Percolate down = O(height) = O(logN)

            Total Complexity = O(logN)

        """
        self.array[1] = self.array[self.size]
        del self.array[self.size]
        self.size -= 1
        self._percolate_down(1)

    def build_heap(self, item_array):
        self.size = len(item_array)
        self.array = [None] + item_array

        for index in reversed(range(1, self.size//2 + 1)):
            self._percolate_down(index)

    def _bubble_up(self, item_index):
        parent_index = item_index//2
        parent = self.array[parent_index]
        if parent is None:
            return
        if parent > self.array[item_index]:
            self.array[item_index], self.array[parent_index] = \
                self.array[parent_index], self.array[item_index]
            self._bubble_up(parent_index)

    def _percolate_down(self, item_index):
        if 2*item_index + 1 <= self.size:
            left_child, right_child = self.array[2*item_index],\
                                      self.array[2*item_index+1]
        elif 2*item_index == self.size:
            left_child, right_child = self.array[2*item_index],\
                                      None
        else:
            return

        if right_child is not None and \
                (right_child < self.array[item_index]) and \
                right_child < left_child:
            self.array[item_index], self.array[2 * item_index + 1] = \
                self.array[2 * item_index + 1], self.array[item_index]
            self._percolate_down(2*item_index + 1)

        elif left_child <= self.array[item_index]:
            self.array[item_index], self.array[2*item_index] = \
                self.array[2*item_index], self.array[item_index]
            self._percolate_down(2*item_index)

    def _get_indices(self, layer, max_width):
        num_indices = 2**layer
        list_indices = [None]*num_indices
        list_indices[0] = max_width//(2*num_indices)

        for i in range(1, num_indices):
            list_indices[i] = list_indices[0]*(1 + 2*i)

        return list_indices

    def _visualize(self, max_char=2):      # max_char in the item
        depth = self._height()
        result = ""
        layer = 0
        max_width = 2**(depth + max_char)

        elements = [1]
        while layer <= depth:
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
                if elements[i] is not None:
                    index = indices[i]
                    str_data = str_data[:index] + \
                           str_data[index:index + 1].\
                               replace(" ", str(self.array[elements[i]])) + \
                           str_data[index + 1:]

            count_elements = len(elements)
            for i in range(count_elements):
                element = elements[0]
                if element is not None:
                    if 2*element + 1 <= self.size:
                        elements.append(2*element)
                        elements.append(2*element + 1)
                    elif 2*element == self.size:
                        elements.append(2*element)
                        elements.append(None)
                    else:
                        elements.append(None)
                        elements.append(None)
                elements.pop(0)

            layer += 1
            result += str_data + "\n"

        return result
