import sys
sys.path.append("../")

from binary_search_tree.binary_search_tree import TreeNode, BinarySearchTree
from copy import deepcopy


class AVLTreeNode(TreeNode):
    def __init__(self,
                 key,
                 payload,
                 height_factor=0,
                 left_child=None,
                 right_child=None,
                 parent=None):
        TreeNode.__init__(self,
                          key,
                          payload,
                          left_child,
                          right_child,
                          parent)
        self.h_factor = height_factor


class AVLTree(BinarySearchTree):
    """
    Implementation constraint: Duplicate entries are not allowed
    """
    def __init__(self):
        BinarySearchTree.__init__(self)

    def __setitem__(self, key, payload):
        """
            Complexity: O(logN)
            Balancing only adds a constant factor to the cost.

        """
        node = AVLTreeNode(key, payload)

        if self.root is None:
            self.root = node
        else:
            return self._insert_node(self.root, node)

    def _insert_node(self, current_node, node):
        if node.key < current_node.key:
            if current_node.left_child:
                self._insert_node(current_node.left_child, node)
            else:
                current_node.left_child = node
                node.parent = current_node
                self._update_factor_insert(node)

        elif node.key > current_node.key:
            if current_node.right_child:
                self._insert_node(current_node.right_child, node)
            else:
                current_node.right_child = node
                node.parent = current_node
                self._update_factor_insert(node)

        else:
            print("Duplicate entry {} is not allowed.".format(node.payload))
            return

    def _update_factor_insert(self, node):
        balanced = node.h_factor in (-1, 0, 1)
        if not balanced:
            self._rebalance(node)
            return

        if node.parent is not None:
            if node.key < node.parent.key:
                node.parent.h_factor += 1

            elif node.key > node.parent.key:
                node.parent.h_factor -= 1

            if node.parent.h_factor is not 0:
                self._update_factor_insert(node.parent)

    def _right_rotation(self, rotating_node):
        root_node = rotating_node.left_child

        rotating_node.left_child = root_node.right_child
        if root_node.right_child is not None:
            root_node.right_child.parent = rotating_node
        root_node.right_child = rotating_node

        if rotating_node.is_root():
            self.root = root_node
        else:
            if rotating_node.key < rotating_node.parent.key:
                rotating_node.parent.left_child = root_node
            else:
                rotating_node.parent.right_child = root_node

        root_node.parent = rotating_node.parent
        rotating_node.parent = root_node

        rotating_node.h_factor = rotating_node.h_factor - \
                                 1 - max(0, root_node.h_factor)

        root_node.h_factor = root_node.h_factor - \
                             1 + min(rotating_node.h_factor, 0)

    def _left_rotation(self, rotating_node):
        root_node = rotating_node.right_child

        rotating_node.right_child = root_node.left_child
        if root_node.left_child is not None:
            root_node.left_child.parent = rotating_node
        root_node.left_child = rotating_node

        if rotating_node.is_root():
            self.root = root_node
        else:
            if rotating_node.key < rotating_node.parent.key:
                rotating_node.parent.left_child = root_node
            else:
                rotating_node.parent.right_child = root_node

        root_node.parent = rotating_node.parent
        rotating_node.parent = root_node

        rotating_node.h_factor = rotating_node.h_factor + \
                                 (1 - min(0, root_node.h_factor))

        root_node.h_factor = root_node.h_factor + \
                             (1 + max(rotating_node.h_factor, 0))

    def _rebalance(self, node):
        if node.h_factor < 0:
            if node.right_child.h_factor > 0:   # Double rotation, inner case
                self._right_rotation(node.right_child)
            self._left_rotation(node)           # Single rotation, outer case

        elif node.h_factor > 0:
            if node.left_child.h_factor < 0:    # Double rotation, inner case
                self._left_rotation(node.left_child)
            self._right_rotation(node)          # Single rotation, outer case

    def _update_factor_delete(self, node):
        if node.parent is not None:
            if node.key < node.parent.key:
                node.parent.h_factor -= 1

            elif node.key > node.parent.key:
                node.parent.h_factor += 1

            balanced = node.parent.h_factor in (-1, 0, 1)
            if not balanced:
                self._rebalance(node.parent)
                node = node.parent

            if node.parent.h_factor not in (-1, 1):
                self._update_factor_delete(node.parent)

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
            if node.left_child:
                node.left_child.parent = replacement_node
            replacement_node.right_child = node.right_child
            if node.right_child:
                node.right_child.parent = replacement_node
            replacement_node.h_factor = node.h_factor
            self.root = replacement_node

    def _delete_node(self, node):
        if node.is_root():
            self._delete_root(node)

        elif node.is_leaf():
            if node.key < node.parent.key:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
            self._update_factor_delete(node)
            del node
            return

        elif node.has_one_child():
            if node.left_child is None:
                if node.key < node.parent.key:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child

                node.right_child.parent = node.parent
                self._update_factor_delete(node)
            else:
                if node.key < node.parent.key:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child

                node.left_child.parent = node.parent
                self._update_factor_delete(node)
            del node
            return

        else:
            min_node = self.find_min(node.right_child)
            replacement_node = deepcopy(min_node)
            self._delete_node(min_node)

            replacement_node.parent = node.parent
            replacement_node.left_child = node.left_child
            if node.left_child:
                node.left_child.parent = replacement_node
            replacement_node.right_child = node.right_child
            if node.right_child:
                node.right_child.parent = replacement_node
            replacement_node.h_factor = node.h_factor
            if node.key < node.parent.key:
                node.parent.left_child = replacement_node
            else:
                node.parent.right_child = replacement_node





