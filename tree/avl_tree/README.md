### Usage

```
avl = AVLTree()

for i in [10 * i for i in range(10)]:
    avl[i] = i

print(avl)
print("Height of the AVL is: {}".format(avl.height))

del avl[65]
data = avl[60]

mode = "inorder"
print("\n" + "=" * 20 + mode + "=" * 20)
for node in avl.traverse(mode):
    print(node.key)

```

```
                                30                               
                 _______________________________                
                |                               |               
                10                              70                
         _______________                 _______________        
        |               |               |               |       
        0               20              50              80         
     _______         _______         _______         _______
    |       |       |       |       |       |       |       |
                                    40      60              90     

Height of the AVL is: 3

====================inorder====================
0
10
20
30
40
50
60
70
80
90

```
