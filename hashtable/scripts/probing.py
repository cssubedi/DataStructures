import sys
sys.path.append("../include/")

from hash_function import *
from get_prime import get_prime_size


class HashNode(object):
    def __init__(self, key=None, data=None, active=True):
        self.key = key
        self.data = data
        self.active = active


class HashFunctionError(Exception): pass


class CollisionResolutionError(Exception): pass


class StrategyError(Exception): pass


class DuplicateInsertionError(Exception): pass


class HashValueError(Exception): pass


class HashWithProbing(object):
    def __init__(self,
                 size,
                 hash_function="simple",
                 collision_resolution="linear_probing"):
        """
        The class implements Hash Table with probing. The class allows three
        techniques for probing:
            Linear probing
            Quadratic probing
            Double Hashing

        """
        self.size = get_prime_size(size)
        self.elements = 0
        self.inactive = 0
        self.__table = [HashNode() for _ in range(self.size)]

        if hash_function is "simple":
            self.__hash_function = simple_hashing
        elif hash_function is "universal":
            self.__hash_function = universal_hashing
        else:
            raise HashFunctionError("Please specify the hash function.")

        if collision_resolution is "linear_probing":
            self.__probing = self.__linear_probing
        elif collision_resolution is "quadratic_probing":
            self.__probing = self.__quadratic_probing
        elif collision_resolution is "double_hashing":
            self.__probing = self.__double_hashing
        else:
            raise CollisionResolutionError("Please specify the collision "
                                          "resolution method.")

    @property
    def load_factor(self):
        """
        Load factor is the fraction of slots occupied or inactive.
            load_factor = number of elements hashed / number of slots
                      a = n / m

        Load factor is maintained below 0.5 to guarantee empty slot with
        quadratic probing.

        """
        while float((self.elements + self.inactive) / self.size) >= 0.5:
            self._rehash()
        return float((self.elements + self.inactive) / self.size)

    def __setitem__(self, key, data):
        """
        Steps:
            Generate hash value = O(1)
            Probe to find first empty slot <= 1/(1-a)
            Insert the item = O(1)

        Expected # of operations <= 2*O(1) + 1/(1-a).

        Rehashing adds O(1) to each insertion

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
            Probe to the slot containing key <= 1/a * ln(1/(1-a))
            (successful search and assuming a < 1)
            Delete the item = O(1)

        Expected # of operations <= 2*O(1) + 1/a * ln(1/(1-a))


        """
        try:
            self.__delete(key)
        except KeyError as e:
            print(e)
            sys.exit(1)

    def __str__(self):
        return self.__visualize(max_char=15)

    def _rehash(self):
        """
        Hash Table is rehashed every time its load factor exceeds 0.5. This
        obviously is a very expensive operation as it is O(N), since N elements
        needs to be inserted again on a new hash __table of size roughly 2N.

        However, rehash only occurs after N/2 insertions and thus only adds
        a constant time cost to each insertion. (O(N)/(N/2) = O(1))

        """
        new_size = get_prime_size(self.size)
        temp_table = self.__table[:]
        self.__table = [HashNode() for _ in range(new_size)]
        self.size = new_size
        self.elements = 0
        for node in temp_table:
            if node.key is not None:
                self.__insert(node.key, node.data)

    def __insert(self, key, data):
        assert self.load_factor < 0.5, "Load factor is not below 0.5."
        hash_value = self.__probing(key)

        if self.__table[hash_value].key == key:
            raise DuplicateInsertionError("Duplicate insertion of key {}.".
                                          format(key))

        self.__table[hash_value].data = data
        self.__table[hash_value].key = key
        self.elements += 1

    def __search(self, key):
        hash_value = self.__probing(key)

        if self.__table[hash_value].key is None:
            raise KeyError("The key {} is not found.".format(key))

        return self.__table[hash_value].data

    def __delete(self, key):
        hash_value = self.__probing(key)

        if self.__table[hash_value].key is None:
            raise KeyError("The key {} is not found.".format(key))

        self.__table[hash_value].data = None
        self.__table[hash_value].key = None
        self.__table[hash_value].active = False

        self.inactive += 1
        self.elements -= 1

    def __linear_probing(self, key):
        """
        Under linear probing, hash function is defined as:

            h(k) = (h'(k) + i) % n
        where h'(k) is called the auxiliary hash function

        """
        index = 0
        hash_value = self.__hash_function(self.size, key)

        while index < self.size:
            new_hash_value = (hash_value + index) % self.size
            if (self.__table[new_hash_value].key is None and
                self.__table[new_hash_value].active) or \
                    self.__table[new_hash_value].key == key:
                return new_hash_value
            index += 1
        raise HashValueError("Could not find an empty slot.")

    def __quadratic_probing(self, key):
        """
        Under quadratic probing, hash function is defined as:

            h(k) = (h'(k) + i^2) % n
        where h'(k) is called the auxiliary hash function

        """
        index = 0
        hash_value = self.__hash_function(self.size, key)

        while index < self.size:
            new_hash_value = (hash_value + index ** 2) % self.size
            if (self.__table[new_hash_value].key is None and
                self.__table[new_hash_value].active) or \
                    self.__table[new_hash_value].key == key:
                return new_hash_value
            index += 1
        raise HashValueError("Could not find an empty slot.")

    def __double_hashing(self, key):
        """
        Double hashing in implemented for the case of string name input.
        Under double hashing, hash function is defined as:

            h(k) = (h1(k) + i * h2(k)) % n
        where h1(k) and h2(k) are called the auxiliary hash functions

        """
        hash_value = self.__hash_function(self.size, key)

        def hash_function2():
            value = 0
            size = len(key)
            for i in range(len(key)):
                value += (ord(key[i]) - 98) * 26 ** (size - i)
            prime = get_prime_size(self.size // 4)
            return prime - (value % prime)                  # never returns 0

        index = 0
        hash_value2 = hash_function2()
        while index < self.size:
            new_hash_value = (hash_value + index * hash_value2) % self.size
            if (self.__table[new_hash_value].key is None and
                self.__table[new_hash_value].active) or \
                    self.__table[new_hash_value].key == key:
                return new_hash_value
            index += 1
        raise HashValueError("Could not find an empty slot.")

    def __visualize(self, max_char):
        output = "\n"
        for node in self.__table:
            if node.key is not None:
                length = len(node.key)
            else:
                length = 4
            spacing = ((max_char-length)//2)
            output += "\t " + "-"*(max_char+2) + "\n" + \
                      "\t" + "| " + " "*spacing + str(node.key) + \
                      " "*(max_char-length-spacing) + " |" + "\n" + \
                      "\t " + "-" * (max_char+2) + "\n"
        return output
