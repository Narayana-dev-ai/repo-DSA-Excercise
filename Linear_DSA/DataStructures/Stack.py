"""
A stack is a data structure that can hold many elements.

Basic operations we can do on a stack are:

    Push: Adds a new element on the stack.
    Pop: Removes and returns the top element from the stack.
    Peek: Returns the top element on the stack.
    isEmpty: Checks if the stack is empty.
    Size: Finds the number of elements in the stack.
    
Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1
        
    def traverseList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("null")
    
    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        
        topNode = self.head
        self.head = self.head.next
        self.size -=1
        return topNode.data
    
    def peek(self):
        if self.isEmpty:
            return "stack is Empty"
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
        
stack = Stack()
stack.push(12)
stack.push(30)
stack.push(1)
stack.traverseList()
print(stack.pop())
stack.traverseList()
print(stack.peek())
print(stack.stackSize())