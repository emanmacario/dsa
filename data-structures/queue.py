from collections import deque

# NB: deque is a list-like container with fast appends and pops on either end

# Definition for queue
class Queue:
    def __init__(self):
        self.queue = deque([])

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return not self.queue
