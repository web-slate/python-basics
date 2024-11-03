print("""
LifoQueue Class:
A Last In, First Out (LIFO) queue, also known as a stack. It is useful when you need a stack-like behavior.
Example: from queue import LifoQueue
""")
from queue import LifoQueue

class CustomLifoQueue:
  def __init__(self):
    self.queue = LifoQueue()

  def enqueue(self, item):
    """Add an item to the end of the queue."""
    self.queue.put(item)

  def dequeue(self):
    """Remove and return the last item from the queue."""
    if not self.is_empty():
      return self.queue.get()
    else:
      print("Queue is empty")
      return None

  def is_empty(self):
    """Check if the queue is empty."""
    return self.queue.empty()

  def size(self):
    """Return the number of items in the queue."""
    return self.queue.qsize()

  def peek(self):
    """Return the last item in the queue without removing it."""
    if not self.is_empty():
      return self.queue.queue[-1]
    else:
      print("Queue is empty")
      return None

# Example usage:
if __name__ == "__main__":
  grocery_queue = CustomLifoQueue()
  print("Initial queue:", list(grocery_queue.queue.queue))

  # Adding people to the queue
  grocery_queue.enqueue("Venkat")
  grocery_queue.enqueue("Suba")
  grocery_queue.enqueue("Gutti")
  print("Queue after adding people:", list(grocery_queue.queue.queue))

  # Serving people from the queue
  serving_person = grocery_queue.dequeue()
  print("Serving:", serving_person)
  print("Queue after serving:", list(grocery_queue.queue.queue))

  # Checking the next person to be served
  next_person = grocery_queue.peek()
  print("Next person to be served:", next_person)
