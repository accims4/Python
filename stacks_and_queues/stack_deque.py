# Python program to 
# demostrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# pop() function to pop
# element from stack in 
# LIFO order
print('\n Elements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)


