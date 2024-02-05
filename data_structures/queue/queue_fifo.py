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

from queue import Queue

# Creating a queue
my_queue = Queue()

def enqueue(data):
  my_queue.put(data)

def dequeue():
  return my_queue.get()

def is_empty():
  return my_queue.empty() 

def peek():
  if is_empty():
    raise IndexError("Queue is empty")
  return my_queue.queue[0]

def contains(person: str):
  return person in my_queue.queue

def print_all_items():
  return list(my_queue.queue)

print("Enqueue  Venkat, Gutti, Suba, and Yuvraj into the queue - using .put()")
enqueue('Venkat')
enqueue('Gutti')
enqueue('Suba')
enqueue('Yuvraj')


print("Show the queue ")
print(print_all_items())
print(''' ''')
print("Dequeue the first person from the queue - using .get()")
person = dequeue()
print(f"Dequeued {person} from the queue" )

print(''' ''')
print("Peek the person from the queue")
person = peek()
print(f"Peek {person} from the queue" )
print(''' ''')

# Check if the queue is empty
print("Checking whether queue is empty or not using .empty() method")
print("Is the queue empty?", is_empty())
print("Show the queue ")
print(print_all_items())
print(''' ''')
print("Check whether suba in the queue or not? ")
print(f"{'suba is in the queue' if contains('Suba') else 'Suba is not in the queue'}")
