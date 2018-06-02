### Usage
```
bst = BinarySearchTree()

bst[1946] = "Mauchly"
bst[1973] = "Knuth"
bst[1623] = "Schickard"
bst[1673] = "Leibniz"
bst[1822] = "Babbage"
bst[1843] = "Lovelace"
bst[1960] = "Lehmer"

print(bst)
print("Height of the BST is: {}".format(bst.height))

del bst[1843]
data = bst[1973]

mode = "inorder"
print("\n" + "=" * 20 + mode + "=" * 20)
for node in bst.traverse("inorder"):
    print(node.key)

```

```
                                                                Mauchly                                                               
                                 _______________________________________________________________                                
                                |                                                               |                               
                                Schickard                                                       Knuth                                       
                 _______________________________                                 _______________________________                
                |                               |                               |                               |               
                                                Leibniz                         Lehmer                                                     
         _______________                 _______________                 _______________                 _______________        
        |               |               |               |               |               |               |               |       
                                                        Babbage                                                                       
     _______         _______         _______         _______         _______         _______         _______         _______ 
    |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |
                                                            Lovelace                                                                   

Height of the BST is: 4

====================inorder====================
1623
1673
1822
1946
1960
1973


```
