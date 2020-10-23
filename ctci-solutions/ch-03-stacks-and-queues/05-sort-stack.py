# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
# Hints: #15, #32, #43


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


def sort(stack):
    """
    Sorts a stack in-place by using an extra stack and no additional
    ephemeral data structures (e.g. an array). The smallest elements
    are at the top of the stack.

    Idea is to transfer all the elements onto the temp stack in reverse
    sorted order, and then reverse the temp stack onto the original stack.
    This is done by popping and testing one element of the original stack,
    and testing it against the temp stack. We reverse the temp stack when
    needed to allow it to be in reverse sorted order at the end.
    """
    tmp = Stack()
    while not stack.is_empty():
        item = stack.pop()

        while not tmp.is_empty() and item < tmp.peek():
            stack.push(tmp.pop())
        
        tmp.push(item)

    while not tmp.is_empty():
        stack.push(tmp.pop())


if __name__ == "__main__":
    stack = Stack.from_list([1, 20, 19, 3, 5, 2, 6, 18, 1])
    print(stack)
    sort(stack)
    print('=' * 25)
    print(stack)
