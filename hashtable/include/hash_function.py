def simple_hashing(hash_size, key):
    """
    This is a simple hashing function example that takes a string as key
    and returns an integer as hash value. The hash function is designed to use
    names of people as keys and store their information in hash __table.
    Only lowercase alphabets are allowed on the key string.

    """
    assert key.isalpha(), "Key is not string with alphabets only."
    assert key.islower(), "Key is not all lowercase."

    value = 0
    size = len(key)
    for i in range(len(key)):
        value += (ord(key[i]) - 96) * 26**(size-i)
    return value % hash_size


from random import randint
HASH_COEFFICIENTS = [randint(0, 256) for _ in range(4)]


def universal_hashing(hash_size, key):
    """
    This is a universal hashing example that takes a string of IPv4 address
    as key and returns an integer hash value.

    Function is defined as such:
    Given an ip address x, which can be represented as a quadruple x = x1.x2.x3.x4

        h_a(x1, x2, x3, x4) = (a1*x1 + a2*x2 + a3*x3 + a4*x4) % m
    where,
        coefficients a = {a1,a2,a3,a4} are randomly selected from {0, m-1}
        m = prime number larger than the expected number of items in hash

    Thus, the family of hash functions is defined as:
        H = {h_a: a = {0,...,m-1}^4}

    """
    elem = key.split(".")

    def valid_ip():
        if len(elem) != 4:
            return False
        for s in elem:
            if not s.isdigit():
                return False
            num = int(s)
            if num < 0 or num > 255:
                return False
        return True

    assert valid_ip(), "The key is not a valid IPv4 address."
    value = 0
    for i in range(len(elem)):
        value += HASH_COEFFICIENTS[i]*int(elem[i])

    return value % hash_size


