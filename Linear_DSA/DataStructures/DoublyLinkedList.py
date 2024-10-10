"""
A doubly linked list has nodes with addresses to both the previous and the next node, like in the image below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\nTraversing Doubly LinkedList Forward")
current_node = node1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("null")

print("\nTraversing Doubly LinkedList Backward")
current_node = node4
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.prev
print("null")