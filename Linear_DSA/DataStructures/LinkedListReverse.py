class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addNode(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
            
    
    def reverseList(self):
        curr = self.head
        prev = None
        
        while curr:
            nextNodes = curr.next
            curr.next = prev
            prev = curr
            curr = nextNodes
            
        self.head = prev

    def findMinValue(self):
        currentNode = self.head
        minVal = currentNode.data
        
        while currentNode:
            if currentNode.data < minVal:
                minVal = currentNode.data
            currentNode = currentNode.next
        
        print("\nSmallest Value in List:",minVal)

        
    def swapNodes(self, val1, val2):
        
        if val1 == val2:
            return 
        
        prevNode1 = None
        currentNode1 = self.head
        while currentNode1 and currentNode1.data != val1:
            prevNode1 = currentNode1
            currentNode1 = currentNode1.next
            
        prevNode2 = None
        currentNode2 = self.head
        while currentNode2 and currentNode2.data != val2:
            prevNode2 = currentNode2
            currentNode2 = currentNode2.next
        
        if currentNode2 is None or currentNode1 is None:
            return
        
        if prevNode1:
            prevNode1.next = currentNode2
        else:
            self.head = currentNode2
        
        if prevNode2:
            prevNode2.next = currentNode1
        else:
            self.head = currentNode1
        
        currentNode1.next, currentNode2.next = currentNode2.next, currentNode1.next
    
    def deleteNode(self, value):
        current = self.head
        prevNode = None
        
        while current and current.data != value:
            prevNode = current
            current = current.next
        if current is None:
            return
        prevNode.next = current.next
        
    def  insertAtPosition(self, value, pos):
        newNode = Node(value)
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
            return 
        
        curr = self.head
        prevNode = None
        for _ in range(2, pos+1, 1):
            if curr.next is None:
                break
            prevNode = curr
            curr = curr.next
            
        
        if curr.next is None:
            curr.next = newNode
        else:
            prevNode.next = newNode
            newNode.next = curr
        
    def traverseList(self):
        current = self.head
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")
        
listObj = SingleLinkList()
listObj.addNode(12)
listObj.addNode(1)
listObj.addNode(9)
listObj.addNode(18)
listObj.addNode(15)

listObj.traverseList()

print("\nAfter Reversing list")
listObj.reverseList()
listObj.traverseList()

print("\nAfter Swaping Nodes")
listObj.swapNodes(15,18)
listObj.traverseList()

print("\nAfter Deleting  node")
listObj.deleteNode(15)
listObj.traverseList()

print("\nAfter Insertion")
listObj.insertAtPosition(69, 2)
listObj.traverseList()

listObj.findMinValue()