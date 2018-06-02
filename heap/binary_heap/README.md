### Usage
```
binary_heap = BinaryHeap()
binary_heap.build_heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

binary_heap.insert(11)
binary_heap.delete_min()

print(binary_heap)

```

```
                1               
         _______________        
        |               |       
        2               4       
     _______         _______
    |       |       |       |
    3       6       5       8
   ___     ___     ___     ___
  |   |   |   |   |   |   |   |
  11  7   9   10


```
