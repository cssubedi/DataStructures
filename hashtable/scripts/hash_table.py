#!/usr/bin/python

from probing import HashWithProbing
from chaining import HashWithChaining


class StrategyError(Exception): pass


class HashTable(object):
    """
    The class instantiates and initializes appropriate hash __table based on
    input parameters. Following parameters characterizes hash __table:
        strategy:
            "chaining": Use separate chaining to store multiple data items
                        into same slots
            "probing": Use open-addressing and perform rehash based on a
                        threshold load factor.
        hash_function:
            "simple": Use the imported simple_hashing function
            "universal": Use the imported universal_hashing function
        collision_resolution:
            "linear_probing": linearly probe in case of collision
            "quadratic_probing": quadratically probe in case of collision
            "double_hashing": use second hash function to probe in case of collision

    """
    def __new__(cls,
                size,
                strategy="chaining",
                hash_function="simple",
                collision_resolution=None):
        if strategy == "chaining":
            new_instance = super().__new__(HashWithChaining,
                                           size,
                                           strategy,
                                           hash_function)
            new_instance.__init__(size, hash_function)
            return new_instance
        elif strategy == "probing":
            new_instance = super().__new__(HashWithProbing,
                                           size,
                                           strategy,
                                           hash_function,
                                           collision_resolution)
            new_instance.__init__(size, hash_function, collision_resolution)
            return new_instance
        else:
            raise StrategyError("Please specify the strategy for collision resolution.")