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

def findMinValue(head):
    min_value = head.data
    
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        
        current_node = current_node.next
    
    return min_value
    
def swapNodes(head, node1, node2):
    prevFirstNode = None
    prevSecondNode = None
    
    if node1 == node2:
        return head
    
    currentFirstNode = head
    while currentFirstNode and currentFirstNode.data != node1:
        prevFirstNode = currentFirstNode
        currentFirstNode = currentFirstNode.next
    
    currentSecondNode = head
    while currentSecondNode and currentSecondNode.data != node2:
        prevSecondNode = currentSecondNode
        currentSecondNode = currentSecondNode.next
        
    if not currentFirstNode or not currentSecondNode:
        return head
    
    if prevFirstNode:
        prevFirstNode.next = currentSecondNode
    else:
        head = currentSecondNode
        
    if prevSecondNode:
        prevSecondNode.next = currentFirstNode
    else:
        head = prevFirstNode
        
    temp = currentFirstNode.next
    currentFirstNode.next = currentSecondNode.next 
    currentSecondNode.next = temp
    
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

print(f"\nMinimum Value From the LinkedList: {findMinValue(node1)}")

# Insert newNode
newNode = Node(69)
node1 = insertAtSpecificPosition(node1, newNode, 7)
print("\nAfter Insertion:")
traverseList(node1)

# Delete node3
node1 = deleteSpecificNode(node1, node3)

print("\nAfter deletion:")
traverseList(node1)

node1 = swapNodes(node1, 7, 69)

print("\nAfter Swaping:")
traverseList(node1)