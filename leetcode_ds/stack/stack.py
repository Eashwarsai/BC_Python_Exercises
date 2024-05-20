# stack.py

class Stack:
    def __init__(self):
        self.items = []

    # CRUD operations for stack

    # Create (Push)
    def push(self, val):
        self.items.append(val)

    # Read (Pop)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # Read (Peek)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Read (is_empty)
    def is_empty(self):
        return len(self.items) == 0

    # Read (size)
    def size(self):
        return len(self.items)
