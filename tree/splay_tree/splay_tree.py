import sys
sys.path.append("../")

from binary_search_tree.binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

    def _zig_right(self, node):
        """
        Performs a single right rotation. Node becomes
        the root of the sub-tree.

        """
        parent_node = node.parent

        parent_node.left_child = node.right_child
        if node.right_child is not None:
            node.right_child.parent = parent_node
        node.right_child = parent_node

        if parent_node.is_root():
            self.root = node
        else:
            if parent_node.key < parent_node.parent.key:
                parent_node.parent.left_child = node
            else:
                parent_node.parent.right_child = node

        node.parent = parent_node.parent
        parent_node.parent = node

    def _zig_left(self, node):
        """
        Performs a single left rotation. Node becomes
        the root of the sub-tree

        """
        parent_node = node.parent

        parent_node.right_child = node.left_child
        if node.left_child is not None:
            node.left_child.parent = parent_node
        node.left_child = parent_node

        if parent_node.is_root():
            self.root = node
        else:
            if parent_node.key < parent_node.parent.key:
                parent_node.parent.left_child = node
            else:
                parent_node.parent.right_child = node

        node.parent = parent_node.parent
        parent_node.parent = node

    def _zig_zig_right(self, node):
        """
            Performs two consecutive right rotations.
            Node becomes the root of the sub-tree

        """
        self._zig_right(node.parent)
        self._zig_right(node)

    def _zig_zig_left(self, node):
        """
        Performs two consecutive left rotations.
            Node becomes the root of the sub-tree

        """
        self._zig_left(node.parent)
        self._zig_left(node)

    def _zig_zag_right(self, node):
        """
        Performs first left and then right rotation.
            Node becomes the root of the sub-tree

        """
        self._zig_left(node)
        self._zig_right(node)

    def _zig_zag_left(self, node):
        """
        Performs first right and then left rotation.
            Node becomes the root of the sub-tree

        """
        self._zig_right(node)
        self._zig_left(node)

    def _get_node(self, key, current_node):
        if not current_node:
            return None
        if key == current_node.key:
            self._rebalance(current_node)
            return current_node
        elif key > current_node.key:
            node = self._get_node(key, current_node.right_child)
        elif key < current_node.key:
            node = self._get_node(key, current_node.left_child)

        return node

    def _rebalance(self, node):
        """
            Performs the necessary rotations to move
            node to the top of the tree.

        """
        if node.is_root():
            return
        elif node.has_grandparent():
            if node.is_left_child():
                if node.parent.is_left_child():
                    self._zig_zig_right(node)
                else:
                    self._zig_zag_left(node)

            else:
                if node.parent.is_right_child():
                    self._zig_zig_left(node)
                else:
                    self._zig_zag_right(node)
        else:
            if node.is_left_child():
                self._zig_right(node)
            else:
                self._zig_left(node)

        if not node.is_root():
            self._rebalance(node)
