class AvlNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print("Rotate right on node", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    
    return x

def leftRotation(x):
    print("Rotate left on node", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    
    return y

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
        
    return current

def deleteNode(node, data):
    if not node:
        return node
    
    if data < node.data:
        node.left = deleteNode(node.left, data)
    elif data > node.data:
        node.right = deleteNode(node.right, data)
    else:
        if node.left is None:
            temp = node.right 
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        else:
            temp = minValueNode(node.right)
            node.data = temp.data
            node.right = deleteNode(node.right ,temp.data)
            
    if node is None:
        return node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)
    
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotation(node.left)
        return rightRotate(node)
    
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotation(node)
    
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotation(node)
    
    return node

def insertNode(node, data):
    if not node:
        return AvlNode(data)
    
    if data < node.data:
        node.left = insertNode(node.left, data)
    elif data > node.data:
        node.right = insertNode(node.right, data)
        
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)
    
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotation(node.left)
        return rightRotate(node)
    
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotation(node)
    
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotation(node)
    
    return node

def inOrderTraversal(node):
    if node is None:
        return 
    inOrderTraversal(node.left)
    print(node.data, end=" -> ")
    inOrderTraversal(node.right)


root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for i in letters:
    root = insertNode(root, i)
    
inOrderTraversal(root)

print("\n After Deletion of E")
deleteNode(root, 'G')
inOrderTraversal(root)