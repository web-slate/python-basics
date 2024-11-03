from stylepy import h1,h2,h3,h4,h5,h6
print('''''')
h1("Circular Queue")
h2('''A circular queue, also known as a ring buffer, is a data structure that effectively uses an array and operates
like a regular queue with a fixed size.
''')
class CircularQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = [None] * capacity
    self.head = 0
    self.tail = 0
    self.size = 0

  def enqueue(self, item):
    if self.size == self.capacity:
      #print("Queue is full. Cannot enqueue new item.") - Implementation 1 
      h4("Queue is full. Overwriting the oldest element.") # Implementation 2 
      self.dequeue() 
    self.queue[self.tail] = item  
    self.tail = (self.tail + 1) % self.capacity  # ( 1 % 4 = 1,  2 % 4 = 2,   ... 4/4 = 0 )
    self.size += 1

  def dequeue(self):
    if self.size == 0:
      h4("Queue is empty")
      return None
    item = self.queue[self.head]
    self.head = (self.head + 1) % self.capacity
    self.size -= 1
    return item

  def peek(self):
    if self.size == 0:
      h4("Queue is empty")
      return None
    return self.queue[self.head]

  def display(self):
    if self.size == 0:
      h4("Queue is empty")
      return
    temp = self.head
    resources = []
    for _ in range(self.size):
      resources.append(self.queue[temp])
      temp = (temp + 1) % self.capacity
    return resources


# Example usage
h3("Database connection pool is initaiated to accommodate 5 resource")
cq = CircularQueue(5)
h4("Resource 1 of 5 is connected")
cq.enqueue("Resource 1")
h4("Resource 2 of 5 is connected")
cq.enqueue("Resource 2")
h4("Resource 3 of 5 is connected")
cq.enqueue("Resource 3")
h4("Resource 4 of 5 is connected")
cq.enqueue("Resource 4")
h4("Resource 5 of 5 is connected")
cq.enqueue("Resource 5")

h3("Display the pool resource")
h4(cq.display())  # Output: 1 2 3 4 5


h3("Which resource will get drop its connect next?")
h4(cq.peek())

h3("Resource 6 is trying to connect")
cq.enqueue("Resource 6")  # Output: Queue is full. Cannot enqueue new item.
h4(cq.display())  # Output: 1 2 3 4 5


h3("Resource 1 is dropped its connection")
cq.dequeue()
h4("Display the pool resource")
h4(cq.display())  # Output: 2 3 4 5


h3("Resource 6 is trying to connect")
cq.enqueue("Resource 6")
h4("There is available place for acceting new connection. New resource is connected successfully")


h3("Display the pool resource")
h4(cq.display())  # Output: 2 3 4 5 6 
