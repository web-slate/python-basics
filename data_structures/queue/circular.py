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
      print("Queue is full. Overwriting the oldest element.") # Implementation 2 
      self.dequeue() 
    self.queue[self.tail] = item  
    self.tail = (self.tail + 1) % self.capacity  # ( 1 % 4 = 1,  2 % 4 = 2,   ... 4/4 = 0 )
    self.size += 1

  def dequeue(self):
    if self.size == 0:
      print("Queue is empty")
      return None
    item = self.queue[self.head]
    self.head = (self.head + 1) % self.capacity
    self.size -= 1
    return item

  def peek(self):
    if self.size == 0:
      print("Queue is empty")
      return None
    return self.queue[self.head]

  def display(self):
    if self.size == 0:
      print("Queue is empty")
      return
    temp = self.head
    resources = []
    for _ in range(self.size):
      resources.append(self.queue[temp])
      temp = (temp + 1) % self.capacity
    return resources


# Example usage
print("Database connection pool is initaiated to accommodate 5 resource")
cq = CircularQueue(5)
print("Resource 1 of 5 is connected")
cq.enqueue("Resource 1")
print("Resource 2 of 5 is connected")
cq.enqueue("Resource 2")
print("Resource 3 of 5 is connected")
cq.enqueue("Resource 3")
print("Resource 4 of 5 is connected")
cq.enqueue("Resource 4")
print("Resource 5 of 5 is connected")
cq.enqueue("Resource 5")
print("------------------------------------")

print("Display the pool resource")
print(cq.display())  # Output: 1 2 3 4 5
print("-----------------------------------")

print("Which resource will get drop its connect next?")
print(cq.peek())
print("-----------------------------------")

print("Resource 6 is trying to connect")
cq.enqueue("Resource 6")  # Output: Queue is full. Cannot enqueue new item.
print(cq.display())  # Output: 1 2 3 4 5
print("------------------------------------")

print("Resource 1 is dropped its connection")
cq.dequeue()
print("Display the pool resource")
print(cq.display())  # Output: 2 3 4 5
print("------------------------------------")

print("Resource 6 is trying to connect")
cq.enqueue("Resource 6")
print("There is available place for acceting new connection. New resource is connected successfully")
print("------------------------------------")

print("Display the pool resource")
print(cq.display())  # Output: 2 3 4 5 6 
