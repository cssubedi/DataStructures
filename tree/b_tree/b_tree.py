import bisect
import math as m


class BTreeLeafNode(object):
    def __init__(self, keys=None, payloads=None, parent=None):
        self.keys = keys
        self.payloads = payloads
        self.parent = parent


class BTreeBranchNode(object):
    def __init__(self, keys=None, children=None, parent=None):
        self.keys = keys
        self.children = children
        self.parent = parent


class BTree(object):
    """
        Implementation constraints:
            1. B+ Tree, a variant of B-Tree is implemented
            2. Q = B.
            3. Duplicate entries not allowed
            4. Dataset contains at least Q/2 items
            5. Order of B-Tree should be greater than 2.

    """
    def __init__(self, order):
        self.order = order
        self.root = None

    @property
    def height(self):
        return self._get_height()

    def __setitem__(self, key, payload):
        """
        Complexity of insertion:
            Inserting into leaf node array = O(B)
            Splitting nodes up to root = O(B)*height

            Total complexity = O(height*B) = O((logN/logB)*B) = O(logN)

        """
        if self.root is None:
            self.root = BTreeLeafNode([key], [payload])
        else:
            return self._insert(key, payload)

    def __getitem__(self, key):
        """
        Complexity of finding the key:
            Searching each node for children = O(logB)
            (Bisect module uses binary search)

            Total complexity = O(height*logB) = O((logN/logB)*logB) = O(logN)

        """
        return self._search(key)

    def __delitem__(self, key):
        """
        Complexity of deleting item:
            Deleting from the leaf node = O(B)
            Merging or Rotating up to root = O(B)*height

            Total complexity  = O(height*B) = O((logN/logN)*B) = O(logN)

        """
        return self._delete(key)

    def __str__(self):
        if self.root:
            return self._visualize()
        else:
            return ""

    def _insert(self, key, payload):
        leaf_node, indices = self._find_leaf(key)
        index = bisect.bisect(leaf_node.keys, key)

        if index != 0 and leaf_node.keys[index - 1] == key:
            print("Duplicated entry {} is not allowed in the {}."
                             .format(payload, self.__class__.__name__))
            return

        leaf_node.keys.insert(index, key)
        leaf_node.payloads.insert(index, payload)

        if self._overflow(leaf_node):
            self._split(leaf_node, indices)

    def _search(self, key):
        leaf_node = self._find_leaf(key)[0]

        try:
            index = leaf_node.keys.index(key)
        except ValueError:
            print("Could not find the key {} in the {}"
                  .format(key, self.__class__.__name__))
            return

        return leaf_node.payloads[index]

    def _delete(self, key):
        leaf_node, indices = self._find_leaf(key)

        try:
            index = leaf_node.keys.index(key)
        except ValueError:
            print("Could not find the key {} in the {}"
                  .format(key, self.__class__.__name__))
            return

        del leaf_node.keys[index]
        del leaf_node.payloads[index]

        if self._underflow(leaf_node):
            self._balance(leaf_node, indices)

    def _get_height(self):
        current_node = self.root
        height = 0

        if current_node is None:
            return height
        else:
            while getattr(current_node, "children", None):
                height += 1
                current_node = current_node.children[0]
            return height

    def _overflow(self, node):
        if getattr(node, "children", None):
            return len(node.children) > self.order
        else:
            return len(node.payloads) > self.order

    def _underflow(self, node):
        if getattr(node, "children", None):
            if node.parent is None:
                return len(node.children) < 2
            else:
                return len(node.children) < m.ceil(self.order/2)
        else:
            return len(node.payloads) < m.ceil(self.order/2)

    def _can_donate(self, node):
        if getattr(node, "children", None):
            return len(node.children) > m.ceil(self.order/2)
        else:
            return len(node.payloads) > m.ceil(self.order/2)

    def _find_leaf(self, key):
        indices = []
        current_node = self.root

        while getattr(current_node, "children", None):
            index = bisect.bisect(current_node.keys, key)
            indices.append(index)
            current_node = current_node.children[index]

        return current_node, indices

    def _split(self, node, parent_indices):
        center = len(node.keys) // 2
        if getattr(node, "children", None):
            new_sibling = BTreeBranchNode(node.keys[center + 1:],
                                          node.children[center + 1:])

            for child in new_sibling.children:
                child.parent = new_sibling
            node.children = node.children[:center+1]
        else:
            new_sibling = BTreeLeafNode(node.keys[center:],
                                        node.payloads[center:])
            node.payloads = node.payloads[:center]

        if node.parent is None:
            self.root = BTreeBranchNode([node.keys[center]])
            new_sibling.parent = self.root
            node.parent = self.root
            self.root.children = [node, new_sibling]
        else:
            new_sibling.parent = node.parent
            node.parent.keys.insert(parent_indices[-1], node.keys[center])
            node.parent.children.insert(parent_indices[-1] + 1, new_sibling)

            if self._overflow(node.parent):
                self._split(node.parent, parent_indices[:-1])

        node.keys = node.keys[:center]

    def _rotate_right(self, node, parent_index):
        sibling = node.parent.children[parent_index - 1]

        if getattr(node, "children", None):
            node.keys.insert(0, node.parent.keys[parent_index - 1])
            node.children.insert(0, sibling.children[-1])
            sibling.children = sibling.children[:-1]
            node.children[0].parent = node

        else:
            node.keys.insert(0, sibling.keys[-1])
            node.payloads.insert(0, sibling.payloads[-1])
            sibling.payloads = sibling.payloads[:-1]

        node.parent.keys[parent_index - 1] = sibling.keys[-1]
        sibling.keys = sibling.keys[:-1]

    def _rotate_left(self, node, parent_index):
        sibling = node.parent.children[parent_index + 1]

        if getattr(node, "children", None):
            node.keys.append(node.parent.keys[parent_index])
            node.children.append(sibling.children[0])
            sibling.children = sibling.children[1:]
            node.children[-1].parent = node
            node.parent.keys[parent_index] = sibling.keys[0]

        else:
            node.keys.append(sibling.keys[0])
            node.payloads.append(sibling.payloads[0])
            sibling.payloads = sibling.payloads[1:]
            node.parent.keys[parent_index] = sibling.keys[1]

        sibling.keys = sibling.keys[1:]

    def _merge_branch(self, node, parent_index):
        if parent_index == 0:
            sibling = node.parent.children[parent_index + 1]
            node.keys.append(node.parent.keys[parent_index])
            del node.parent.keys[parent_index]

            node.keys += sibling.keys
            node.children += sibling.children

            for child in sibling.children:
                child.parent = node
            del node.parent.children[parent_index + 1]

        else:
            sibling = node.parent.children[parent_index - 1]
            sibling.keys.append(node.parent.keys[parent_index - 1])
            del node.parent.keys[parent_index - 1]

            sibling.keys += node.keys
            sibling.children += node.children

            for child in node.children:
                child.parent = sibling
            del node.parent.children[parent_index]

    def _merge_leaf(self, node, parent_index):
        if parent_index == 0:
            del node.parent.keys[parent_index]
            sibling = node.parent.children[parent_index + 1]

            node.keys += sibling.keys
            node.payloads += sibling.payloads
            del node.parent.children[parent_index + 1]
        else:
            del node.parent.keys[parent_index - 1]
            sibling = node.parent.children[parent_index - 1]

            sibling.keys += node.keys
            sibling.payloads += node.payloads
            del node.parent.children[parent_index]

    def _merge(self, node, parent_index):
        if getattr(node, "children", None):
            self._merge_branch(node, parent_index)
        else:
            self._merge_leaf(node, parent_index)

    def _balance(self, node, indices):
        if node.parent is None:
            if getattr(node, "children", None):
                self.root = node.children[0]
                self.root.parent = None
                del node
            return

        parent_index = indices[-1]
        if parent_index > 0 and \
                self._can_donate(node.parent.children[parent_index - 1]):

            self._rotate_right(node, parent_index)

        elif parent_index < len(node.parent.children) - 1 and \
                self._can_donate(node.parent.children[parent_index + 1]):

            self._rotate_left(node, parent_index)

        else:
            self._merge(node, parent_index)

            if self._underflow(node.parent):
                self._balance(node.parent, indices[:-1])

    def _get_indices(self, layer, max_char, spacing):
        num_indices = self.order**layer
        list_indices = [None]*num_indices

        for i in range(0, num_indices):
            list_indices[i] = ((max_char + spacing) *
                               ((2*i+1)*self.order**(self.height-layer) - 1))//2

        return list_indices

    def _visualize(self, key_len=3, spacing=2): # key_len = max char in the key.
        max_char = self.order*(key_len + 2)
        result = "\n" + ""
        layer = 0
        max_width = (max_char + spacing)*self.order**self.height

        nodes = [self.root]
        while layer <= self.height:
            str_data = " " * max_width
            indices = self._get_indices(layer, max_char, spacing)
            len_indices = len(indices)

            if len_indices > 1:
                str_underscore = " " * max_width
                str_bar = " " * max_width
                for i in range(len_indices // self.order):
                    start = indices[self.order * i]
                    end = indices[self.order*(i+1)-1]
                    str_underscore = str_underscore[:start + 1] + \
                                     str_underscore[start + 1:end].replace(" ","_") + \
                                     str_underscore[end:]
                result += str_underscore + "\n"

                for index in indices:
                    str_bar = str_bar[:index] + \
                              str_bar[index:index+1].replace(" ", "|") + \
                              str_bar[index+1:]
                result += str_bar + "\n"

            for i in range(len_indices):
                if nodes[i] is not None:
                    index = indices[i]
                    if getattr(nodes[i], "children", None):
                        data = str(tuple(nodes[i].keys))
                    else:
                        data = str(nodes[i].keys)
                    str_data = str_data[:index] + \
                               str_data[index:index + 1].replace(" ", data) + \
                               str_data[index + 1:]

            count_nodes = len(nodes)
            for i in range(count_nodes):
                node = nodes[0]
                if node is None:
                    nodes += [None]*(self.order)
                elif getattr(node, "children", None):
                    nodes += node.children + (self.order -
                                              len(node.children))*[None]
                nodes.pop(0)

            layer += 1
            result += str_data + "\n"

        return result





