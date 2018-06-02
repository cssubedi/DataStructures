### Usage
```
splay_tree = SplayTree()
splay_tree[10] = 'P'
splay_tree[90] = 'Q'
splay_tree[100] = 'R'
splay_tree[70] = 'S'
splay_tree[60] = 'T'
splay_tree[50] = 'A'

print(splay_tree)
print("Height of the Splay Tree is: {}".format(splay_tree.height))

splay_tree[60]

print(splay_tree)
print("Height of the Splay Tree is: {}".format(splay_tree.height))
```

```
                                                                P                                                               
                                 _______________________________________________________________                                
                                |                                                               |                               
                                                                                                Q                               
                 _______________________________                                 _______________________________                
                |                               |                               |                               |               
                                                                                S                               R               
         _______________                 _______________                 _______________                 _______________        
        |               |               |               |               |               |               |               |       
                                                                        T                                                       
     _______         _______         _______         _______         _______         _______         _______         _______
    |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
                                                                    A                                                           

Height of the Splay Tree is: 4
                                T                               
                 _______________________________                
                |                               |               
                P                               S               
         _______________                 _______________        
        |               |               |               |       
                        A                               Q       
     _______         _______         _______         _______
    |       |       |       |       |       |       |       |
                                                            R   

Height of the Splay Tree is: 3

```
