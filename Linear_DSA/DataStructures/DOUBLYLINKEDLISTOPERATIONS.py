class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

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
    current_node = head
    
    firstNode = None
    secondNode = None
    
    while current_node:
        if current_node.data == node1:
            firstNode = current_node
        if current_node.data == node2:
            secondNode = current_node
            
        current_node = current_node.next
   

    temp = firstNode.next
    firstNode.next = secondNode.next
    secondNode.next = temp
    
    if firstNode.next != None:
        firstNode.next.prev = firstNode
    if secondNode.next != None:
        secondNode.next.prev = secondNode
    
    temp = firstNode.prev
    firstNode.prev = secondNode.prev
    secondNode.prev = temp
    
    if firstNode.prev != None:
        firstNode.prev.next = firstNode
    if secondNode.prev != None:
        secondNode.prev.next = secondNode

    
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
node1 = insertAtPosition(node1, newNode, 5)

print("\nAfter Insertion")
traverseList(node1)


node1 = deleteNode(node1, 19)

print("\nAfter Deletion")
traverseList(node1)

node1 = swapNodes(node1, 24, 4)

print("\nAfter Swaping Numbers")
traverseList(node1)