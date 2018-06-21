### Usage
##### Separate Chaining
```
hash_table = HashTable(3, "chaining", "simple")

hash_table.insert("christie", "09/27/1991")
hash_table.insert("david", "09/27/1993")
hash_table.insert("madeline", "09/23/1991")

print("\n"+ "="*8 + " Hash Table " + "="*8)
print(hash_table)

del hash_table['david']
data = hash_table['christie']

```

```
======== Hash Table ========

     -----------------
    |      None       |
     -----------------
     -----------------
    |      david      |---> christie
     -----------------
     -----------------
    |    madeline     |
     -----------------

```
##### Probing (Linear, Quadratic and Double Hashing)
```
hash_table = HashTable(4, "probing", "simple", "linear_probing")
hash_table.insert("christie", "09/27/1991")
hash_table.insert("david", "09/27/1993")
hash_table.insert("madeline", "09/23/1991")
hash_table.insert("sam", "10/27/1996")

print("\n"+ "="*8 + " Hash Table " + "="*8)
print(hash_table)

del hash_table['david']
data = hash_table['christie']

```
```
======== Hash Table ========

     -----------------
    |      None       |
     -----------------
     -----------------
    |    christie     |
     -----------------
     -----------------
    |       sam       |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    |    madeline     |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    |      david      |
     -----------------

```
##### Universal Hashing with Chaining
```
hash_table = HashTable(5, "chaining", "universal")
from random import randint
ips = []
for i in range(5):
    ip = ""
    for _ in range(4):
        ip += str(randint(0, 255)) + "."
    ips.append(ip[:-1])

for ip in ips:
    hash_table[ip] = ip
print("\n"+ "="*8 + " Hash Table " + "="*8)
print(hash_table)
```

```
======== Hash Table ========

     -----------------
    |  171.94.75.17   |
     -----------------
     -----------------
    |  3.118.164.193  |
     -----------------
     -----------------
    | 142.254.204.218 |
     -----------------
     -----------------
    |  206.10.57.29   |
     -----------------
     -----------------
    | 154.132.166.100 |
     -----------------

```
##### Universal Hashing with Probing
```
hash_table = HashTable(5, "probing", "universal", "double_hashing")
from random import randint
ips = []
for i in range(5):
    ip = ""
    for _ in range(4):
        ip += str(randint(0, 255)) + "."
    ips.append(ip[:-1])

for ip in ips:
    hash_table[ip] = ip
print("\n"+ "="*8 + " Hash Table " + "="*8)
print(hash_table)

```

```
======== Hash Table ========

     -----------------
    |      None       |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    | 189.221.80.211  |
     -----------------
     -----------------
    |  23.129.234.94  |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    |  251.20.244.12  |
     -----------------
     -----------------
    |      None       |
     -----------------
     -----------------
    |  189.29.175.72  |
     -----------------
     -----------------
    | 178.98.230.148  |
     -----------------
     -----------------
    |      None       |
     -----------------
```
