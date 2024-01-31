
class QueueSimple:

  def __init__(self):
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0 
  
  def enqueue(self, data):
    self.queue.append(data)

  def dequeue(self): 
    if not self.is_empty():
      self.queue.pop(0)
    else: 
      raise IndexError("Queue is empty and unable to dequeue")
    
  def size(self):
    return len(self.queue)
  
  def display(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    return ','. join([str(i) for i in self.queue])
  
queue = QueueSimple()
for i in range(10, 50, 10):
  queue.enqueue(i) 
print("Queue items", queue.display())

print("Dequeue from the queue item")
queue.dequeue()
print("Queue item after dequeue", queue.display())

