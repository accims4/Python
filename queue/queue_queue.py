# Python program to 
# demostrate implementation of 
# queue using queue module

from Queue import Queue

# Initializing a queue
queue = Queue(maxsize=3)

# qsize() gice the maxsize
# of the Queue
print(queue.qsize())

# Adding of element to queue
queue.put('a')
queue.put('b')
queue.put('c')

# Return boolean for full
# Queue
print("\nFull: ", queue.full())

# Removing element from queue 
print("\nElements dequeued from the queue")
print(queue.get())
print(queue.get())
print(queue.get())

# Return boolean from empty
# Queue
print("\nEmpty: ", queue.empty())

queue.put(1)
print("\nEmpty: ", queue.empty()) 
print("\nFull: ", queue.full())