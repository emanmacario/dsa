# Successor: Write an algorithm to find the "next" node (i.e., in-order 
# successor) of a given node in a binary search tree. You may assume that 
# each node has a link to its parent.
# Hints: #79, #9z


# Definition for a binary search tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if not self.right:
                self.right = TreeNode(val, parent=self)
            else:
                self.right.insert(val)
        else:
            if not self.left:
                self.left = TreeNode(val, parent=self)
            else:
                self.left.insert(val)

    def __str__(self):
        return str(self.val)

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
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
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
        

# -- Debugging

def in_order_traversal(node):
    """
    Visit left branch, then current node, then right branch
    """
    if node:
        in_order_traversal(node.left)
        print(node.val)
        in_order_traversal(node.right)


# -- Solution

def in_order_successor(node):
    """
    Finds and returns the in-order successor of a given node in a tree
    """
    if not node:
        return None

    # Right child exists, return leftmost node in right subtree
    if node.right:
        return leftmost_child(node.right)
    else:
        n = node
        p = n.parent
        # Go up until we're on left instead of right
        while p and p.left is not n:
            n = p
            p = p.parent
        return p


def leftmost_child(node):
    """
    Returns leftmost node in the given subtree
    """
    if not node:
        return None
    
    while node.left:
        node = node.left

    return node


# -- Testing

from random import randint, seed

if __name__ == "__main__":
    seed(69)
    tree = TreeNode(50)
    for _ in range(20):
        tree.insert(randint(25, 75))
    tree.display()

    print('---\nIn-order traversal:\n')
    in_order_traversal(tree)
    print('---')
    print(in_order_successor(tree.right.left.left.right))
    