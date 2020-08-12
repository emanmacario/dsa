# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
# Hints: #64, #87


# Definition for stack
class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
        self.size = 0

    def push(self, item):
        if not self.is_full():
            self.size += 1
            self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return not self.stack or self.size == 0

    def is_full(self):
        return self.size == self.capacity

    @classmethod
    def from_list(cls, vals):
        stack = Stack()
        for val in vals:
            if not stack.is_full():
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


class SetOfStacks:
    """
    A class that supports multiple finite sized stacks
    """

    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, item):
        last = self._get_last_stack()
        if last and not last.is_full():
            # Add to last stack
            last.push(item)
        else:
            # Must create new stack
            stack = Stack(self.capacity)
            stack.push(item)
            self.stacks.append(stack)
        

    def pop(self):
        last = self._get_last_stack()
        if last:
            if not last.is_empty():
                # Pop item from non-empty last stack
                return last.pop()
            else:
                # Last stack is empty, remove from stacks
                self.stacks.pop()


    def pop_at(self, index):
        # Too convoluted for coding interview. Read solutions
        pass


    def _get_last_stack(self):
        return self.stacks[-1] if self.stacks else None


    def __str__(self):
        s = ''
        for stack in self.stacks:
            s += f'{stack.__str__()}\n'
            s += '~' * 25 + '\n'
        return s


if __name__ == "__main__":
    set_of_stacks = SetOfStacks(2)
    set_of_stacks.push(1)
    set_of_stacks.push(2)
    set_of_stacks.push(3)
    set_of_stacks.push(4)
    set_of_stacks.push(5)
    print(set_of_stacks)
    set_of_stacks.pop()
    print(set_of_stacks)
    set_of_stacks.pop()

