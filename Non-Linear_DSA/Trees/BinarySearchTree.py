"""
A Binary Search Tree is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.
A clear advantage with Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.

How it works:

    Start at the root node.
    If this is the value we are looking for, return.
    If the value we are looking for is higher, continue searching in the right subtree.
    If the value we are looking for is lower, continue searching in the left subtree.
    If the subtree we want to search does not exist, depending on the programming language, return None, or NULL, or something similar, to indicate that the value is not inside the BST.

To check if a Binary Tree is BST, is to do an in-order traversal (like we did on the previous page) and check if the resulting list of values are in an increasing order.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insertNode(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.data:
            root.left = insertNode(root.left, value)
        elif value > root.data:
            root.right = insertNode(root.right, value)
    return root

def minValue(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def maxValue(root):
    current = root
    while current.right is not None:
        current = current.right
    return current

def isBST(root):
    if root is None:
        return True
    
    if root.left and maxValue(root.left).data >= root.data:
        return False
    if root.right and minValue(root.right).data <= root.data:
        return False
    
    return isBST(root.left) and isBST(root.right)
    

def deleteNode(root, value):
    if not root:
        return None
    
    if value < root.data:
        root.left = deleteNode(root.left, value)
    elif value > root.data:
        root.right = deleteNode(root.right, value)
    else:
        if not root.left:
            temp = root.right
            root =  None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        else:
            root.data = minValue(root.right).data
            root.right = deleteNode(root.right, root.data)
            
    return root
            

def preOrderTraverse(root):
    if root is None:
        return
    print(root.data, end=" -> ")
    preOrderTraverse(root.left)
    preOrderTraverse(root.right)
    
def postOrderTraverse(root):
    if root is None:
        return
    postOrderTraverse(root.left)
    postOrderTraverse(root.right)
    print(root.data, end=" -> ")
    
def inOrderTraverse(root):
    if root is None:
        return
    inOrderTraverse(root.left)
    print(root.data, end=" -> ")
    inOrderTraverse(root.right)
    
def binarySearch(root, value):
    if root is None:
        return None
    elif root.data == value:
        return root
    elif root.data < value:
        return binarySearch(root.right, value)
    else:
        return binarySearch(root.left, value)
        
        
root = Node(13)
node7 = Node(7)
node15 = Node(15)
node3 = Node(3)
node8 = Node(8)
node14 = Node(14)
node19 = Node(19)
node18 = Node(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

print("\nIn Order Traversal...")
inOrderTraverse(root)

result = binarySearch(root, 19)
print("\nResult: ", result.data)

print("\nAfter Inserting 10")
inserResult = insertNode(root, 10)
inOrderTraverse(inserResult)

print("\nAfter Deleting 19")
delResult = deleteNode(root, 13)
inOrderTraverse(delResult)

print("\nCheck is BST or NOT:", isBST(root))
