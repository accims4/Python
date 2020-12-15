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
        return None(key)
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