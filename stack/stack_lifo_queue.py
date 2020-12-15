# Python program to 
# demostrate stack implementation
# using queue module

from Queue import LifoQueue

# Initializing a stack
stack = LifoQueue(max_size = 3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')  
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in 
# LIFO order
print('\nElement poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

    