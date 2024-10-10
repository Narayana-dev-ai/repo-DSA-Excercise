"""

A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer. The way they are linked together is that each node points to where in the memory the next node is placed.
A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.

"""

class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1
while current_node:
    print(f"Node Data: {current_node.data}")
    current_node = current_node.next
    
print("Finished List Travelling...")