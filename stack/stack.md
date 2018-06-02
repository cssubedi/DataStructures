### Stack
Stack data structure facilitates Last In First Out (LIFO) relation for the data access. There are two implementation techniques:
* Array based implementation
* Linked List based implementation

It is similar to list except that insert/delete operations are allowed only at the beginning of the list (top of the stack). The table belows shows complexities of different operations for array based Stack implementation.

| Operation | Description | Complexity  |
| --------- | ----------  | ----------  |
| $push$    | Insert at the top                           | $O(1)$  |
| $pop$     | Remove the top item                         | $O(1)$  |
| $top$     | Return the top item, without altering Stack | $O(1)$  |
| $top\_pop$| Return and remove the top element           | $O(1)$  |
| $is\_empty$| Return True if Stack is empty, else False  | $O(1)$  |
| $make\_empty$| Empty the Stack                          | $O(1)$  |

For Linked List implementation, $make\_empty$ operation takes $\Theta(N)$ time
