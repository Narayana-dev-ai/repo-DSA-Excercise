class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.head = None
        
    def getHeight(self, root):
        if root is None:
            return 0
        
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        
    def findMinValue(self):
        root = self.head
        
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        
        print("\nMinimum value in the BST is:",root.data)
        
    def createBinarySearchTree(self, array):
        root = self.head
        
        def createBstFromArray(array, low, high):
            if low > high:
                return None
        
            mid = (low + high) //2
            root = Node(array[mid])
        
            root.left = createBstFromArray(array, low, mid-1)
            root.right = createBstFromArray(array, mid+1, high)
        
            return root
        self.head = createBstFromArray(array, 0, len(array)-1)
    
    def inOrderTraverse(self):
        root = self.head
        
        def printData(root):
            if root is None:
                return None
            printData(root.left)
            print(root.data, end=" -> ")
            printData(root.right)
        printData(root)

inOrderArray = [1, 2, 5, 10, 15, 20, 30]

bstObj = BST()
bstObj.createBinarySearchTree(inOrderArray)
bstObj.inOrderTraverse()
bstObj.findMinValue()
print(f"Height of BST is: {bstObj.getHeight(bstObj.head)}")
