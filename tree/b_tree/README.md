### Usage
```
my_btree = BTree(3)
for i in [10*i for i in range(10)]:
    my_btree[i] = i

del my_btree[50]
data = my_btree[40]

print(my_btree)
print("Height of the B-Tree of order {} is {}.".format(my_btree.order, my_btree.height))

```
```

                                                                    (40,)                                                                                    
                  _____________________________________________________________________________________________________                                  
                 |                                                  |                                                  |                                 
                 (20,)                                              (80,)                                                                                        
 _________________________________                  _________________________________                  _________________________________                 
|                |                |                |                |                |                |                |                |                
[0, 10]          [20, 30]                          [40, 60, 70]     [80, 90]                                                                                                            

Height of the B-Tree of order 3 is 2.
```
