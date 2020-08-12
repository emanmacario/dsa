# Definition for stack
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

    @classmethod
    def from_list(cls, vals):
        stack = Stack()
        for val in vals:
            stack.push(val)
        return stack

    def __str__(self):
        if self.is_empty():
            return 'EMPTY'
        s = ''
        for val in self.stack[::-1]:
            s += f'|{val:2}|\n'
        s += '----'
        return s


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(-2)
    print(stack)
    
    s2 = Stack.from_list([1, 2, 3, 6, 2, 4])
    print(s2)
