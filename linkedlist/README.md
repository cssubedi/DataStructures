### Usage
```
llist = SinglyLinkedList()
llist.add("Morse")
llist.add("Boole")
llist.add("Turing")
llist.add("Knuth")
print(llist)

llist.remove("Boole")

print((llist))
print(len(llist))
print("Morse" in llist)

```

```
	 --------        --------        --------        --------        
	| Knuth  | ---> | Turing | ---> | Boole  | ---> | Morse  | --->
	 --------        --------        --------        --------        

	 --------        --------        --------        
	| Knuth  | ---> | Turing | ---> | Morse  | --->
	 --------        --------        --------        
3
True

```

```
llist = DoublyLinkedList()
llist.add("Morse")
llist.add("Boole")
llist.add("Turing")
llist.add("Knuth")
print(llist)

llist.remove("Boole")

print((llist))
print(len(llist))
print("Elon" in llist)

```

```
	 --------        --------        --------        --------        
	| Knuth  | <--> | Turing | <--> | Boole  | <--> | Morse  | <-->
	 --------        --------        --------        --------        

	 --------        --------        --------        
	| Knuth  | <--> | Turing | <--> | Morse  | <-->
	 --------        --------        --------        
3
False


```
