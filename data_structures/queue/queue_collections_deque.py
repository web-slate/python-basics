from stylepy import h1,h2,h3
h2("""
- collections.deque in Python is a mutable data structure, and you can add, remove, or modify elements.
- It is a double-ended queue, optimized for fast operations at both ends.

""")

from collections import deque
h1("initialise the queue using deque ")
# Creating a deque
my_deque = deque([10, 4, 5, 8])

print("adding value 25 to the right - using .append()")
# Adding an element to the right
my_deque.append(25)
print("Print the queue items")
h3(my_deque)  # Output: deque([10, 4, 5, 8, 25])

print("removing item from the left -  fifo using .popleft()")
# Removing an element from the left
removed_element = my_deque.popleft()
print("Removed element:", removed_element)  # Output: Removed element: 10
h3(my_deque)  # Output: deque([4, 5, 8, 25])


# Removing an element from the right
print("removing item from the right -  lifo using .pop()")
removed_element = my_deque.pop()
print("Removed element:", removed_element)  # Output: Removed element: 25
h3(my_deque)  # Output: deque([4, 5, 8])
