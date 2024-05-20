
from leetcode_ds.linkedlist import *
from leetcode_ds import Stack
from leetcode_ds import Queue
print(dir())
# Use the data structures
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.display()

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.front())
