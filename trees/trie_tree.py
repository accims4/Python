# Python program to 
# demostrate common operations 
# trie tree (aka prefix tree)
 
# A utility class that represents 
# an individual node in a trie
class Node: 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
