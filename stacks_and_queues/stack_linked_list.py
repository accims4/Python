# Python program to demostrate
# stack implementation using a linked list

# node class
class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack: 
    
    # initializing a stack
    # using a dummy node, which is 
    # easier for handling edges cases
    def __init__ (self): 
        self.head = Node("head")
        self.size = 0

    # string representation of the stack
    def __str__(self): 
        current = self.head.next
        output = ""
        while current:
            output += str(current.data) + "->"
            current = current.next
        return output[:-3]

    # get the current size of the stack
    def getSize(self):
        return self.size

    # check if the stack is empty
    def isEmpty(self): 
        return self.size == 0

    # get the top of the stack
    def peek(self): 

        # sanitary check to see if we 
        # are peeking an empty stack
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # push a value into the stack
    def push (self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    # remove a value from the stack and return 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return remove.value

# driver code
if __name__ == "__main__": 
    stack = Stack()
    for i in range( 1, 11): 
        stack.push(i)
    print("Stack:{}".format(stack))

    for _ in range( 1, 6):
        remove = stack.pop()
        print("Pop: {}".format(remove))
    print("Stack:{}".format(stack))
