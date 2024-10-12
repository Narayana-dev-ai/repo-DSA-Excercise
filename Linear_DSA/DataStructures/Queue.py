"""
A queue is a data structure that can hold many elements.

Basic operations we can do on a queue are:

    Enqueue: Adds a new element to the queue.
    Dequeue: Removes and returns the first (front) element from the queue.
    Peek: Returns the first element in the queue.
    isEmpty: Checks if the queue is empty.
    Size: Finds the number of elements in the queue.
    
Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, value):
        newNode = Node(value)
        if self.rear is None:
            self.front = self.rear = newNode
            self.size += 1
            return
        self.rear.next = newNode
        self.rear = newNode
        self.size += 1
        
    def traverseList(self):
        currentNode = self.front
        
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("null")
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
            
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.data
        
    def isEmpty(self):
        return self.size == 0
    
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(17)
queue.enqueue(5)
queue.enqueue(24)
queue.traverseList()
print(queue.dequeue())
queue.traverseList()
print(queue.peek())