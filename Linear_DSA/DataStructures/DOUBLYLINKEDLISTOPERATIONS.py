class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
def traverseReverseOrder(head):
    current_node = head
    while current_node.next:
        current_node = current_node.next
        
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.prev
    print("null")

def traverseList(head):
    current_node = head
        
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")
    
def insertAtPosition(head, node, pos):
    if pos == 1:
        node.next = head
        head.prev = node
        return node
    
    current_node = head
    for _ in range(pos-2):
        if current_node.next is None:
            break
        current_node = current_node.next
    
    node.next = current_node.next
    node.prev = current_node
    current_node.next = node
    
    return head

def deleteNode(head, node):
    if head.data == node:
        return head.next
    
    current_node = head.next
    while current_node and current_node.data != node:
        current_node = current_node.next
    
    if current_node is None:
        print("\nElement Not Found")
    else:
        current_node.prev.next = current_node.next
    
    
    return head

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
        
    if prevFirstNode:
        prevFirstNode.next = currentSecondNode
    else:
        head = currentSecondNode
        
    if prevSecondNode:
        prevSecondNode.next = currentFirstNode
    else:
        head = currentFirstNode
        
    temp = currentFirstNode.next
    currentFirstNode.next = currentSecondNode.next
    currentSecondNode.next = temp
    
    if currentFirstNode.next:
        currentFirstNode.next.prev = currentFirstNode
    if currentSecondNode.next:
        currentSecondNode.next.prev = currentSecondNode
        
    temp = currentFirstNode.prev
    currentFirstNode.prev = currentSecondNode.prev
    currentSecondNode.prev = temp
    
    if currentFirstNode.prev:
        currentFirstNode.prev.next = currentFirstNode
    if currentSecondNode.prev:
        currentSecondNode.prev.next = currentSecondNode
    
    return head
    
        
node1 = Node(14)
node2 = Node(24)
node3 = Node(4)
node4 = Node(19)
node5 = Node(50)


node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3

node5.prev = node4


print("Before Any Operatiion")
traverseList(node1)

newNode = Node(99)
iNode = insertAtPosition(node1, newNode, 5)

print("\nAfter Insertion")
traverseList(iNode)

dNode = deleteNode(node1, 19)

print("\nAfter Deletion")
traverseList(dNode)

sNodes = swapNodes(dNode, 50, 14)

print("\nAfter Swaping Numbers")
traverseList(sNodes)
traverseReverseOrder(sNodes)