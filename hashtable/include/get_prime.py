import pkg_resources


def get_prime_size(size):
    data_file = pkg_resources.resource_filename("hashtable", "/data/primes.txt")
    if (size & (size - 1)) != 0:
        size = 2**(len(bin(size)[2:]))

    with open(data_file, "r+") as filename:
        lines = filename.readlines()[1:]
        for line in lines:
            elements, prime = line.strip().split(",")
            if size == int(elements):
                return int(prime)
