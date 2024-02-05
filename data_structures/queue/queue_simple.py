
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
  
  def print_all_items(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    return ','. join([str(i) for i in self.queue])
  
queue = QueueSimple()
for i in ['Suba', 'Venkat' ,'Gutti', 'Yuvraj']:
  queue.enqueue(i) 

print("Queue: ", queue.print_all_items())

print("Dequeue the person from the queue")
queue.dequeue()
print("Queue: ", queue.print_all_items())

