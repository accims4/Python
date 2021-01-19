# Python program to 
# demostrate common operations 
# in binary search tree
 
# A utility class that represents 
# an individual node in a BST
class Node: 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert
# a new node with the given key
def insert(root, key):
    if root is None: 
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else: 
            root.left = insert(root.left, key)
    return root

# A utility function search a given key is BST
def search(root, key): 

    # Base Cases: root is null or key is presented at root
    if root is None or root.val == key: 
        return root
    
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# A utility function to do inorder tree traversal
def inorder(root):
    if root: 
        inorder(root.left)
        print(root.val)
        inorder(root.right)   

# A utility function to do preorder tree traversal
def preorder(root):
    if root: 
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# A utility function to do postorder tree traversal
def postorder(root):
    if root: 
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Driver program to test functions above
r = Node(50)
r = insert(r, 80)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 40)
r = insert(r, 30)
r = insert(r, 20)
print("---------------------")
inorder(r)
print("---------------------")
preorder(r)
print("---------------------")
postorder(r)
