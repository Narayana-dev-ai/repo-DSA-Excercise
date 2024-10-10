"""
Basic things we can do with linked lists are:

    Traversal
    Remove a node
    Insert a node
    Sort
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseList(head):
    current_node = head
    
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

def deleteSpecificNode(head, deleteNode):
    if head == deleteNode:
        return head.next
    
    current_node = head
    
    while current_node.next and current_node.next != deleteNode:
        current_node = current_node.next
    
    if current_node.next is None:
        return head
    
    current_node.next = current_node.next.next
    
    return head
        
def insertAtSpecificPosition(head, insertNode, pos):
    if pos == 1:
        insertNode.next = head
        return insertNode
    
    current_node = head
    for _ in range(pos-2):
        if current_node.next is None:
            break
        current_node = current_node.next
   
    if current_node is None:
        current_node.next = newNode
    else:
        newNode.next = current_node.next
        current_node.next = newNode
    
    return head
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before Any Operation:")
traverseList(node1)

# Insert newNode
newNode = Node(69)
node1 = insertAtSpecificPosition(node1, newNode, 7)
print("\nAfter Insertion:")
traverseList(node1)

# Delete node3
node1 = deleteSpecificNode(node1, node3)

print("\nAfter deletion:")
traverseList(node1)