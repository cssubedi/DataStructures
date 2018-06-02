from copy import deepcopy


class TreeNode(object):
    def __init__(self,
                 key,
                 payload,
                 left_child=None,
                 right_child=None,
                 parent=None):
        self.key = key
        self.payload = payload
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def __eq__(self, other):
        return self.key == other.key

    def is_leaf(self):
        return self.right_child is None and self.left_child is None

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        if self.is_root():
            return False
        else:
            return self.key < self.parent.key

    def is_right_child(self):
        if self.is_root():
            return False
        else:
            return self.key > self.parent.key

    def has_one_child(self):
        return self.left_child is None or self.right_child is None

    def has_grandparent(self):
        try:
            return self.parent.parent is not None
        except AttributeError:
            return False


class BinarySearchTree(object):
    """
    Implementation constraints: Duplicate entries are not allowed
    """
    def __init__(self):
        self.root = None

    def __setitem__(self, key, payload):
        """
        Complexity: O(height of BST)

        """
        node = TreeNode(key, payload)

        if self.root is None:
            self.root = node
        else:
            return self._insert_node(self.root, node)

    def __contains__(self, key):
        """
        Complexity: O(height of BST)

        """
        if self._get_node(key, self.root) is None:
            return False
        else:
            return True

    def __getitem__(self, key):
        """
        Complexity: O(height of BST)

        """
        node = self._get_node(key, self.root)
        if node is None:
            return None
        else:
            return node.payload

    def __delitem__(self, key):
        """
        Complexity: O(logN)

        When the height of BST is O(N), deletion happens
        in constant time as each node only has one child.
        This is a tighter bound compared to O(height of BST).

        """
        node = self._get_node(key, self.root)
        if node is None:
            return
        else:
            self._delete_node(node)

    def __str__(self):
        node = self.root
        if node is not None:
            return self._visualize()
        else:
            return ""

    @property
    def height(self):
        """
        Complexity: O(2N + 1) = O(N)

        height: Max number of edges from root to a leaf in BST

        """
        return max(self._get_height(self.root), 0)

    def traverse(self, mode="inorder"):
        if mode == "inorder":
            return self._inorder_traversal(self.root)
        elif mode == "preorder":
            return self._preorder_traversal(self.root)
        elif mode == "postorder":
            return self._postorder_traversal(self.root)
        else:
            return ["Could not traverse. "
                    "Please specify the mode of traversal: "
                    "inorder or preorder or postorder"]

    def find_min(self, current_node):
        """
        Complexity: O(log(N+1)) = O(logN)

        """
        if current_node.left_child is None:
            return current_node
        else:
            return self.find_min(current_node.left_child)

    def find_max(self, current_node):
        """
        Complexity: O(log(N+1)) = O(logN)

        """
        if current_node.right_child is None:
            return current_node
        else:
            return self.find_max(current_node.right_child)

    def _get_height(self, node):
        if node is None:
            return -1
        else:
            return max(self._get_height(node.left_child), self._get_height(node.right_child)) + 1

    def _insert_node(self, current_node, node):

        if node.key < current_node.key:
            if current_node.left_child:
                self._insert_node(current_node.left_child, node)
            else:
                current_node.left_child = node
                node.parent = current_node

        elif node.key > current_node.key:
            if current_node.right_child:
                self._insert_node(current_node.right_child, node)
            else:
                current_node.right_child = node
                node.parent = current_node

        else:
            raise ValueError("Duplicate entry {} is not allowed in {}."
                             .format(node.payload, self.__class__.__name__))

    def _get_node(self, key, current_node):
        if not current_node:
            return None
        if key == current_node.key:
            return current_node
        elif key > current_node.key:
            node = self._get_node(key, current_node.right_child)
        elif key < current_node.key:
            node = self._get_node(key, current_node.left_child)

        return node

    def _delete_root(self, node):
        if node.is_leaf():
            self.root = None
            del node
            return

        elif node.has_one_child():
            if node.left_child is None:
                self.root = node.right_child
                self.root.parent = None
            else:
                self.root = node.left_child
                self.root.parent = None
            del node
            return

        else:
            min_node = self.find_min(node.right_child)
            replacement_node = deepcopy(min_node)
            self._delete_node(min_node)

            replacement_node.parent = node.parent
            replacement_node.left_child = node.left_child
            replacement_node.right_child = node.right_child
            self.root = replacement_node

    def _delete_node(self, node):
        if node.is_root():
            self._delete_root(node)

        elif node.is_leaf():
            if node.key < node.parent.key:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
            del node
            return

        elif node.has_one_child():
            if node.left_child is None:
                if node.key < node.parent.key:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child

                node.right_child.parent = node.parent
            else:
                if node.key < node.parent.key:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child

                node.left_child.parent = node.parent
            del node
            return

        else:
            min_node = self.find_min(node.right_child)
            replacement_node = deepcopy(min_node)
            self._delete_node(min_node)

            replacement_node.parent = node.parent
            replacement_node.left_child = node.left_child
            replacement_node.right_child = node.right_child
            if node.key < node.parent.key:
                node.parent.left_child = replacement_node
            else:
                node.parent.right_child = replacement_node

    def _inorder_traversal(self, current_node):
        if current_node is not None:
            for node in self._inorder_traversal(current_node.left_child):
                yield node
            yield current_node
            for node in self._inorder_traversal(current_node.right_child):
                yield node

    def _preorder_traversal(self, current_node):
        if current_node is not None:
            yield current_node
            for node in self._preorder_traversal(current_node.left_child):
                yield node
            for node in self._preorder_traversal(current_node.right_child):
                yield node

    def _postorder_traversal(self, current_node):
        if current_node is not None:
            for node in self._postorder_traversal(current_node.left_child):
                yield node
            for node in self._postorder_traversal(current_node.right_child):
                yield node
            yield current_node

    def _get_indices(self, layer, max_width):
        num_indices = 2**layer
        list_indices = [None]*num_indices
        list_indices[0] = max_width//(2*num_indices)

        for i in range(1, num_indices):
            list_indices[i] = list_indices[0]*(1 + 2*i)

        return list_indices

    def _visualize(self, max_char=3):
        result = ""
        layer = 0
        max_width = 2**(self.height + max_char)

        nodes = [self.root]
        while layer <= self.height:
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
                           str_data[index:index + 1].replace(" ", str(nodes[i].payload)) + \
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
