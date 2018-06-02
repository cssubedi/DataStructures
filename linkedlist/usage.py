from LinkedList import SinglyLinkedList, DoublyLinkedList

if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.add("Morse")
    llist.add("Boole")
    llist.add("Turing")
    llist.add("Knuth")
    print(llist)
    llist.remove("Boole")
    print((llist))
    print(len(llist))
    print("Morsdfe" in llist)