print("""
What is priority Queue? 
- The elements in the priority queue are tuples, and the priority is determined by the first element of each tuple. 
- The element with the lowest value in the first position will have the highest priority
- Elements are popped from the queue based on their priority. Lower values have higher priority.
- The elements are dequeued in ascending order of priority.
- In case of ties in priority, the elements are dequeued in the order they were added.
""")

from queue import PriorityQueue

class CustomPriorityQueue:
  def __init__(self):
    self.queue = PriorityQueue()

  def enqueue(self, person: str, priority: int):
    """Add an item to the queue with a specified priority."""
    self.queue.put((priority, person)) 
    
  def dequeue(self):
    """Remove and return the item with the highest priority from the queue."""
    if not self.is_empty():
      return self.queue.get()[1] 
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
    """Return the item with the highest priority in the queue without removing it."""
    if not self.is_empty():
      return self.queue.queue[0][1]
    else:
      print("Queue is empty")
      return None


if __name__ == "__main__":
  grocery_queue = CustomPriorityQueue()
  print("Initial queue:", list(grocery_queue.queue.queue))

  # Adding people to the queue with priorities
  grocery_queue.enqueue("Venkat", 2)
  grocery_queue.enqueue("Suba", 1)
  grocery_queue.enqueue("Gutti", 3)
  print("Queue after adding members:", list(grocery_queue.queue.queue))

  # Serving people from the queue
  serving_person = grocery_queue.dequeue()
  print("Serving:", serving_person)
  print('''-----------------------------------''')
  print("Queue after serving:", list(grocery_queue.queue.queue))

  # Checking the next person to be served
  next_person = grocery_queue.peek()
  print("Next person to be served:", next_person)
  print('''-----------------------------------''')
  print("")
  print("Yuvaraj is our platinum member. Giving him higher priority")
  grocery_queue.enqueue('Yuvaraj', 1)
  print("Karthi is also our platinum member. Giving him higher priority too")
  print("")
  grocery_queue.enqueue('Karthi', 1)

  print('Queue after adding platinum members', grocery_queue.queue.queue)
  print('''-----------------------------------''')
  print("Next person to be served:", grocery_queue.peek())

  print("Serving:", grocery_queue.dequeue())

