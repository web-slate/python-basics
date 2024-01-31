print("""
Queue Class:
The basic FIFO queue. It is often used for thread-safe communication between threads in a multithreaded environment.
Example: from queue import Queue

LifoQueue Class:
A Last In, First Out (LIFO) queue, also known as a stack. It is useful when you need a stack-like behavior.
Example: from queue import LifoQueue

PriorityQueue Class:
A priority queue, where elements are dequeued based on their priority. Elements must be comparable.
Example: from queue import PriorityQueue

""")

from queue import LifoQueue

# Creating a queue
my_queue = LifoQueue()

def display(my_queue: LifoQueue):
  items = []
  while not my_queue.empty():
    items.append(my_queue.get())
  return items

# Enqueue elements
print("Put item 1, 2, 3 into the queue - using .put()")
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)
print(list(my_queue.queue))

# Dequeue elements
print("get(pop) the item from the queue - using .get()")
element = my_queue.get()
print("Dequeued element:", element)

# Check if the queue is empty
print("Checking whether queue is empty or not using .empty() method")
is_empty = my_queue.empty()
print("Is the queue empty?", is_empty)

print("Queue items - convert to list and display")
print(list(my_queue.queue))


