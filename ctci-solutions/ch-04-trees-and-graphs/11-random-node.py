# Random Node: You are implementing a binary tree class from scratch which, in 
# addition to insert, find, and delete, has a method getRandomNode() which 
# returns a random node from the tree. All nodes should be equally likely to be 
# chosen. Design and implement an algorithm for getRandomNode, and explain how 
# you would implement the rest of the methods.
# Hints: #42, #54, #62, #75, #89, #99, #112, #119


# -- Solution

from random import randint, randrange, seed


class TreeNode:
    """
    A tree data structure that supports random retriedata of nodes
    from the tree, where each node has equal probability, 1/N, of being
    chosen. The tree node data structure is modified to store the total 
    number of descendant nodes it has to allow for 'truly' random retriedata.
    We consider a node to be a descendant of itself.

    Algorithmic Complexity:
        - In a balanced tree, takes O(log N), where N is total number of nodes
        - More generally, takes O(H) where H is height of tree
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1
    
    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        index = randrange(0, self.size)  # Index in range [0, size)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert(self, data):
        if data <= self.data:
            if not self.left:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
        self.size += 1

    def search(self, data):
        if self.data == data:
            return self
        elif data <= self.data:
            return self.left.search(data) if self.left else None
        else:
            return self.right.search(data) if self.right else None


    # -- Utility functions  

    def __str__(self):
        """
        Returns string representation of node's dataue
        """
        return str(self.data)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """
        Returns list of strings, width, height, and 
        horizontal coordinate of the root
        """
        # No child
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# -- Testing

if __name__ == "__main__":
    # seed(100)
    tree = TreeNode(20)
    for _ in range(20):
        tree.insert(randint(0, 40))
    tree.display()

    print('\n--- Random Nodes ---')
    for _ in range(10):
        print(tree.get_random_node())
