class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node('R')
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeC.right = nodeH

print("root.left.right.data --> D ==", root.left.right.data)