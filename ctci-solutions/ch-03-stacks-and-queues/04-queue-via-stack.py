# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
# Hints: #98, #114


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return not self.stack

    def __str__(self):
        if self.is_empty():
            return 'EMPTY'
        s = ''
        for val in self.stack[::-1]:
            s += f'|{val:2}|\n'
        s += '----'
        return s


class MyQueue:
    def __init__(self):
        self.q = Stack()
        self.tmp = Stack()

    def enqueue(self, val):
        self.q.push(val)

    def dequeue(self):
        # Check if queue is empty
        if self.q.is_empty():
            return None

        # Reverse the stack into the 'tmp' stack
        while not self.q.is_empty():
            n = self.q.pop()
            self.tmp.push(n)

        # Get value of queue head
        head = self.tmp.pop()

        # Un-reverse the stack into the original stack 'q'
        while not self.tmp.is_empty():
            n = self.tmp.pop()
            self.q.push(n)

        return head

    def is_empty(self):
        return self.q.is_empty()

    def peek(self):
        # Check if queue is empty
        if self.q.is_empty():
            return None

        # Reverse the stack into the 'tmp' stack
        while not self.q.is_empty():
            n = self.q.pop()
            self.tmp.push(n)

        # Get value of queue head
        head = self.tmp.peek()

        # Un-reverse the stack into the original stack 'q'
        while not self.tmp.is_empty():
            n = self.tmp.pop()
            self.q.push(n)


        return head


if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # 2
    print(queue.dequeue())  # 3
    print(queue.dequeue())  # None
    queue.enqueue(4)
    print(queue.peek())     # 4
    print(queue.dequeue())  # 4


    