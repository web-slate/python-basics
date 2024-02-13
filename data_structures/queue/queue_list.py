class Queue:
    def __init__(self):
      self.items = []

    def enqueue(self, item):
      """Add an item to the end of the queue."""
      self.items.append(item)

    def dequeue(self):
      """Remove and return the first item from the queue."""
      if not self.is_empty():
        return self.items.pop(0)
      else:
        print("Queue is empty")
        return None

    def is_empty(self):
      """Check if the queue is empty."""
      return len(self.items) == 0

    def size(self):
      """Return the number of items in the queue."""
      return len(self.items)

    def peek(self):
      """Return the first item in the queue without removing it."""
      if not self.is_empty():
        return self.items[0]
      else:
        print("Queue is empty")
        return None

# Example usage:
if __name__ == "__main__":
  grocery_queue = Queue()
  print("Initial queue:", grocery_queue.items)

  # Adding people to the queue
  grocery_queue.enqueue("Venkat")
  grocery_queue.enqueue("Suba")
  grocery_queue.enqueue("Gutti")
  print("Queue after adding people:", grocery_queue.items)

  # Serving people from the queue
  serving_person = grocery_queue.dequeue()
  print("Serving:", serving_person)
  print("Queue after serving:", grocery_queue.items)

  # Checking the next person to be served
  next_person = grocery_queue.peek()
  print("Next person to be served:", next_person)
