# Route Between Nodes: Given a directed graph, design an algorithm to find out 
# whether there is a route between two nodes.
# Hints: #127

# Definition for queue
class Queue:
    def __init__(self):
        self.queue = deque([])

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return not self.queue


class Graph:
    def __init__(self):
        pass


def search(graph, start, end):
    if start is end:
        return True

    queue = Queue()
    


if __name__ == "__main__":
    pass