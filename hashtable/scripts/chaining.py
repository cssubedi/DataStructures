import sys
sys.path.append("../include/")
from hash_function import *
from linked_list import LinkedList


class HashFunctionError(Exception): pass


class DuplicateInsertionError(Exception): pass


class HashWithChaining(object):
    def __init__(self, size, hash_function="simple"):
        """
        Implementation constraint: Duplicate entries are not allowed
        """
        self.size = size
        self.elements = 0
        self.__table = [LinkedList() for _ in range(self.size)]

        if hash_function is "simple":
            self.__hash_function = simple_hashing
        elif hash_function is "universal":
            self.__hash_function = universal_hashing
        else:
            raise HashFunctionError("Please specify the hash function.")

    @property
    def load_factor(self):
        return round(self.elements / self.size, 2)

    def __setitem__(self, key, data):
        """
        In this implementation, duplicate keys are not allowed. Thus before
        insertion, it is checked if the key already exists.

        Steps:
            Generate hash value = O(1)
            Check for duplicates = load_factor = a
            Insert the data = O(1)

        Expected # of operations = Big-Theta(1 + a)

        """
        try:
            self.__insert(key, data)
        except DuplicateInsertionError as e:
            print(e)
            sys.exit(1)

    def __getitem__(self, key):
        try:
            return self.__search(key)
        except KeyError as e:
            print(e)
            sys.exit(1)

    def __delitem__(self, key):
        """
        Steps:
            Generate hash value = O(1)
            Search for the node containing key = a
            Delete the key = O(1)

        Expected # of operations = Big-Theta(1 + a)

        """
        try:
            self.__delete(key)
        except KeyError as e:
            print(e)
            sys.exit(1)

    def __str__(self):
        return self.__visualize(max_char=15)

    def __insert(self, key, data):
        hash_value = self.__hash_function(self.size, key)
        if key in self.__table[hash_value]:
            raise DuplicateInsertionError("Duplicate insertion.")

        self.__table[hash_value].add(key, data)
        self.elements += 1

    def __search(self, key):
        hash_value = self.__hash_function(self.size, key)
        data = self.__table[hash_value].search(key)
        if data is None:
            raise KeyError("The key {} is not found".format(key))
        return data

    def __delete(self, key):
        hash_value = self.__hash_function(self.size, key)
        self.__table[hash_value].remove(key)
        self.elements -= 1

    def __visualize(self, max_char):
        output = "\n"
        for llist in self.__table:
            if llist.head is not None:
                length = len(llist.head.key)
                key = str(llist.head.key)
            else:
                length = 4
                key = str(None)
            spacing = ((max_char-length)//2)
            output += "\t " + "-"*(max_char+2) + "\n" + \
                      "\t" + "| " + " "*spacing + key + \
                      " "*(max_char-length-spacing) + " |"
            for node in llist:
                if node is not None and llist.head != node:
                    output += "---> " + str(node.key)

            output += "\n" + "\t " + "-" * (max_char+2) + "\n"

        return output
