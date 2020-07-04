from collections import deque
# Optimized to add or remove elements from both ends

# Create a new empty double ended queue (dequeue) that will function as
# a queue. Queue is first in first out, i.e. add at one end and remove at
# another end.

queue = deque()


# TODO: Add some items to the queue.

queue.append(1)
queue.append(21)
queue.append(31)
queue.append(41)
queue.append(51)

print(queue)

# Pop off an item from the front of the list. i.e. pop left

x = queue.popleft()
print(f"Element popped off from front: {x}")

print(f"Queue after popping an element off: {queue}")
