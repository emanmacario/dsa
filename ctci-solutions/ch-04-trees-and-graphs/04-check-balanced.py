# Check Balanced: Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree 
# such that the heights of the two subtrees of any node never differ by more 
# than one.
# Hints: #21, #33, #49, #105, #124


# Definition for a binary search tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        else:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)

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

def minimal_tree(vals):
    """
    Creates a binary search tree with minimal
    height given an array of sorted integers
    """
    if not vals:
        return None
    
    n = len(vals)
    root = TreeNode(vals[n // 2])
    root.left = minimal_tree(vals[0 : n//2])
    root.right = minimal_tree(vals[n // 2 + 1:])
    return root


# -- Solution

def check_balanced(root):
    """
    This code runs in O(N) time and O(H) space, 
    where H is the height of the tree
    """
    return check_height(root) != float('-inf')


def check_height(root):
    if not root:
        return -1
    
    left_height = check_height(root.left)
    if left_height == float('-inf'):
        # Pass error up
        return float('-inf')

    right_height = check_height(root.right)
    if right_height == float('-inf'):
        # Pass error up
        return float('-inf')
    
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return float('-inf')
    
    return max(left_height, right_height) + 1


# -- Testing

from random import randint


if __name__ == "__main__":
    root = TreeNode(50)
    for _ in range(10):
        root.insert(randint(25, 75))
    root.display()
    print(check_balanced(root))  # True or False

    print('-' * 50)
    minimal = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8])
    minimal.display()
    print(check_balanced(minimal))  # True

