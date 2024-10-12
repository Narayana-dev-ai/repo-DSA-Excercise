class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
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
        
root = Node('R')
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeI = Node('I')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeC.right = nodeH

nodeF.left = nodeI

print("root.left.right.data --> D ==", root.left.right.data)

print("\nPre Order Traverse...")
preOrderTraverse(root)

print("\nIn Order Traverse...")
inOrderTraverse(root)

print("\nPost Order Traverse...")
postOrderTraverse(root)