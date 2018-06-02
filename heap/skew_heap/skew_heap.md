### Skew Heap
Skew heap is very similar to the Leftish heap, except that there is no structural constraint through npl. It is a self-balancing version of Leftish heap, just like Splay tree is self-balancing version of AVL tree.

Instead of conditionally swapping children as in Leftish Heap, children are always swapped during $merge$ routine. This is what keeps right path of the Skew Heap small on average. However, worst-case length of the right path is still $O(N)$. And consequently, the worst-case running time of all operation is $O(N)$.

For $M$ consecutive operations on Splay Tree, the worst-case total running time is $O(MlogN)$. Thus, the amortized complexity of an operation is $O(logN)$

##### An open problem
What is the expected length of the right path for Leftish and Skew Heap?
