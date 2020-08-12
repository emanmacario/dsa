# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Hints: #27, #59, #78


class MinStack:
    """
    Idea of getting minimum stack value in O(1) time is for each node in the stack to keep track of
    the minimum value for all nodes below it (including itself). Thus, when we pop, we do not have to
    perform O(N) search for new min

    NB: Each node in the stack is (MIN, VALUE)

    Assumptions:
        - Methods pop, top and getMin operations will always be called on non-empty stacks
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        currMin = self.getMin()
        currMin = min(currMin, x) if currMin is not None else x
        self.stack.append((currMin, x))

    def pop(self) -> None:
        # Return nothing
        self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1][0]

    def __str__(self):
        if not self.stack:
            return 'EMPTY'

        s = ''
        for node in self.stack[::-1]:
            s += f'{node}\n'
        return s


if __name__ == "__main__":
    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    print(stack)
    print(f'MIN: {stack.getMin()}')
