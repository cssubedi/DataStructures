### Usage
#### Undirected graph
```
ugraph = UGraph()
ugraph.add_vertex('A')
ugraph.add_vertex('B')
ugraph.add_vertex('E')
ugraph.add_vertex('F')

ugraph.add_edge('A', 'B')
ugraph.add_edge('A', 'E')

print(ugraph)

n, alist = ugraph.connected_components()
print("{} connected components are: {}".format(n, str(alist)[1:-1]))

ugraph.remove_vertex("F")
ugraph.remove_edge("A", "B")

```

```
A---->B---->E
|
|
B---->A
|
|
E---->A
|
|
F

2 connected components are: ['A', 'B', 'E'], ['F']

```
#### Directed Graph
```
dgraph = DGraph()

dgraph.add_vertex('G')
dgraph.add_vertex('H')
dgraph.add_vertex('I')
dgraph.add_vertex('J')
dgraph.add_vertex('K')
dgraph.add_vertex('L')

dgraph.add_edge('G', 'I')
dgraph.add_edge('H', 'L')
dgraph.add_edge('I', 'J')
dgraph.add_edge('J', 'G')
dgraph.add_edge('J', 'L')
dgraph.add_edge('K', 'H')
dgraph.add_edge('L', 'K')

print(dgraph)

print("Acyclic: {}".format(dgraph.acyclic))

print("Linearized graph is: {}".format(dgraph.linearize()))

n, alist = dgraph.strongly_connected_components()
print("{} strongly connected components are: {}".format(n, str(alist)[1:-1]))

dgraph.remove_vertex("I")
dgraph.remove_edge("H", "L")

```
```
G---->I
|
|
H---->L
|
|
I---->J
|
|
J---->G---->L
|
|
K---->H
|
|
L---->K

Acyclic: False
Linearized graph is: The graph is cyclic and cannot be linearized.
2 strongly connected components are: ['H', 'L', 'K'], ['G', 'I', 'J']

```
