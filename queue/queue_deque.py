# Python program to 
# demostrate queue implementation
# using collections.deque


from collections import deque

# Initializing a queue 
queue = deque()

# Adding elements to a queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elements")
print(queue)
