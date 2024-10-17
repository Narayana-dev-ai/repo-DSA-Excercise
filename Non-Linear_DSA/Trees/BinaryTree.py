class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.head = None
        
        
    def addIntoBST(self, value):
        root = self.head
        
        def innerInsert(root, value):
            if root is None:
                root = Node(value)
            else:
                if value > root.data:
                    root.right = innerInsert(root.right, value)
                elif value < root.data:
                    root.left = innerInsert(root.left, value)
            return root
        
        self.head = innerInsert(root, value)
    
    def deleteNodeFromBST(self, value):
        root = self.head
        
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
                    root = None
                    return temp
                elif not root.right:
                    temp = root.left
                    root = None
                    return temp
                else:
                    root.data = self.minValue(root.right).data
                    root.right = deleteNode(root.right, root.data)
                
            return root
                
        
        self.head = deleteNode(root, value)
        
    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
            
        return current
    
    def maxValue(self, node):
        current = node
        while current.right is not None:
            current = current.right
            
        return current
        
    def isBinarySearchTree(self):
        root = self.head
        
        def checkBSTCases(root):
            if root is None:
                return True
            
            if root.left and self.maxValue(root.left).data >= root.data:
                return False
            
            if root.right and self.minValue(root.right).data < root.data:
                return False
            
            return checkBSTCases(root.left) and checkBSTCases(root.right)
        
        
        return checkBSTCases(root)
    
    def preOrderTraverse(self):
        root = self.head
        def printdata(root):
            if root is None:
                return
            print(root.data, end=" -> ")
            printdata(root.left)
            printdata(root.right)
            
        printdata(root)
        
    def postOrderTraverse(self):
        root = self.head
        def printdata(root):
            if root is None:
                return
            printdata(root.left)
            printdata(root.right)
            print(root.data, end=" -> ")
            
        printdata(root)
        
    def inOrderTraverse(self):
        root = self.head
        def printdata(root):
            if root is None:
                return
            printdata(root.left)
            print(root.data, end=" -> ")
            printdata(root.right)
            
        printdata(root)
             
             
             
bstObject = BinarySearchTree()
bstObject.addIntoBST(100)
bstObject.addIntoBST(20)
bstObject.addIntoBST(10)
bstObject.addIntoBST(30)
bstObject.addIntoBST(200)
bstObject.addIntoBST(150)
bstObject.addIntoBST(300)

print("\nPre Order Traversal is")
bstObject.preOrderTraverse()

print("\nChecking the BST Rules Passed:",bstObject.isBinarySearchTree())

print("\nIn Order Traversal is")
bstObject.inOrderTraverse()

print("\nAfter Deletion of 100 InorderTraverse")
bstObject.deleteNodeFromBST(100)
bstObject.inOrderTraverse()