# queue.py

class Queue:
    def __init__(self):
        self.items = []

    # CRUD operations for queue

    # Create (Enqueue)
    def enqueue(self, val):
        self.items.append(val)

    # Read (Dequeue)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    # Read (Front)
    def front(self):
        if not self.is_empty():
            return self.items[0]

    # Read (Rear)
    def rear(self):
        if not self.is_empty():
            return self.items[-1]

    # Read (is_empty)
    def is_empty(self):
        return len(self.items) == 0

    # Read (size)
    def size(self):
        return len(self.items)
