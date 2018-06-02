### Usage
```
tree = GenericTree()

tree.add_subtree('A', ['B', 'C'])
tree.add_subtree('B', ['E', 'A'])
tree.add_subtree('C', ['G', 'H'])

print("=" * 20 + " Tree " + "=" * 20)
print(tree)

print("Height of the tree is: {}".format(tree.height))

tree.move('B', 'H')

print("=" * 20 + " Tree " + "=" * 20)
print(tree)

print("Height of the tree is: {}".format(tree.height))

```

```
==================== Tree ====================
    [ A ]
    |
    |--->[ B ]
    |    |
    |    |--->[ E ]
    |    |
    |    |--->[ A ]
    |
    |--->[ C ]
    |    |
    |    |--->[ G ]
    |    |
    |    |--->[ H ]

Height of the tree is: 2
==================== Tree ====================
    [ A ]
    |
    |--->[ C ]
    |    |
    |    |--->[ G ]
    |    |
    |    |--->[ H ]
    |    |    |
    |    |    |--->[ B ]
    |    |    |    |
    |    |    |    |--->[ E ]
    |    |    |    |
    |    |    |    |--->[ A ]

Height of the tree is: 4

```
