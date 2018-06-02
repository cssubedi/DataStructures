### Usage
```
d_sets = DisjointSet(20)

for i in range(20):
    modulo = i % 5
    d_sets.union_by_height(i, modulo)

print(d_sets)
print(d_sets.find(18))

```
```
[[0, 5, 10, 15], [1, 6, 11, 16], [2, 7, 12, 17], [3, 8, 13, 18], [4, 9, 14, 19]]
8

```
