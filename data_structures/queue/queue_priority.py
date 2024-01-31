print("""
- Elements are popped from the queue based on their priority. Lower values have higher priority.
- The elements are dequeued in ascending order of priority. In case of ties in priority,
    the elements are dequeued in the order they were added.
- The elements in the priority queue are tuples, and the priority is determined by the first element of each tuple. 
- The element with the lowest value in the first position will have the highest priority
""")

print("""
PriorityQueue uses a heap data structure internally 
      to efficiently maintain the order of elements based on their priorities
""")



print("""
the ordering of strings in the PriorityQueue is based on lexicographical order,
which means it's based on the ASCII values of the characters.
The comparison is done character by character from left to right,
and the first differing character determines the order.

""")
from queue import PriorityQueue

# Creating a priority queue
my_priority_queue = PriorityQueue()

# Enqueue elements with priority
my_priority_queue.put((3, "Task 3"))  # Priority 3
my_priority_queue.put((1, "Task 1"))  # Priority 1
my_priority_queue.put((2, "Task 2"))  # Priority 2

# Dequeue elements based on priority
while not my_priority_queue.empty():
  priority, task = my_priority_queue.get()
  print(f"Processed task '{task}' with priority {priority}")
