### Splay Tree
Splay tree is a self balancing binary tree that performs $splaying$ after certain ADT operations like $insert / find$. A popular choice is to perform $splaying$ after each $find$ operation. The idea is based on the heuristic that an element accessed now will be accessed again in future. The accessed element $X$ is moved to the top of the tree through multiple AVL rotations such that, tree as a whole is more balanced.

There are six rotational operations:
* $Zig \ right$: A single right rotation
* $Zig \ left$: A single left rotation
* $Zig-Zig \ right$: A double right rotation
* $Zig-Zig \ left$: A double left rotation
* $Zig-Zag \ right$: First left and then right rotation
* $Zig-Zag \ left$: First right and then left rotation

The illustration below shows how rotations are chosen. There are two factors in play:
* Whether the accessed node has grandparents
* Whether the accessed node is left child or right child

##### Access B: $Zig \ right$ rotation

              A                                 |B|
            /   \                               /   \
         |B|      C          ===>             D       A       
        /   \                               /   \     
      D       E                           E       C

##### Access C: $Zig \ left$ rotation

              A                                 |C|
            /   \                              /   \
          B      |C|         ===>            A       E       
                /   \                      /   \     
              D       E                  B       D

##### Access D: $Zig-Zig \ right$ rotation

              A                                  B                            |D|
            /   \                              /   \                             \
          B      C           ===>           |D|      A            ===>             B
        /   \                                      /   \                             \
      |D|     E                                  E       C                            A
                                                                                    /   \
                                                                                  E       C

##### Access E: $Zig-Zig \ left$ rotation

              A                                 C                                     |E|
            /   \                             /   \                                 /
          B       C          ===>           A       |E|           ===>            C
                /   \                     /   \                                 /
              D      |E|                B       D                             A
                                                                            /   \
                                                                          B       D

##### Access E: $Zig-Zag \ right$ rotation

              A                                 A                               |E|
            /   \                             /   \                            /   \
           B      C          ===>          |E|      C             ===>       B       A
         /   \                             /                                /          \
       D      |E|                        B                                D              C
                                        /
                                      D


##### Access D: $Zig-Zag \ left$ rotation

              A                                 A                               |D|
            /   \                             /   \                            /   \
          B       C          ===>           B     |D|             ===>       A       C
                /   \                                \                      /          \
             |D|     E                                C                   B              E
                                                        \
                                                          E

Any sequence of $M$ operations on Splay tree takes $O(MlogN)$ time. So, the amortized running time of one operation is $O(logN)$. Splay tree guarantees that even though an operation can take $O(N)$ time, it is impossible to get long $O(N)$ operation sequences. In absence of splaying, $M$ operations can take $O(MN)$ time.
