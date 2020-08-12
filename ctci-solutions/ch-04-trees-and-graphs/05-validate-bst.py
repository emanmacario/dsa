# Validate BST: Implement a function to check if a binary tree is a binary 
# search tree.
# Hints: #35, #57, #86, #113, #128
from random import randint


# Definition for a binary tree node
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


def validate_bst(root):
    """
    Time complexity is O(N). Solution keeps track of the minimum and 
    maximum values for each recursive call at a particular depth, that
    act as constraints for a particular node's value. Space complexity
    is O(N), which occurs when stack space is of size N, which occurs
    when tree is skewed
    """
    return validate_bst_util(root, float('-inf'), float('inf'))


def validate_bst_util(node, low, high):
    """
    Helper function for validating a binary search tree
    """
    if not node:
        return True

    if not low < node.val < high:
        return False

    return validate_bst_util(node.left, low, node.val) and \
           validate_bst_util(node.right, node.val, high)
    


if __name__ == "__main__":
    invalid_tree = TreeNode(4, TreeNode(5), TreeNode(6))
    invalid_tree.display()
    print(validate_bst(invalid_tree))
    print('~' * 25)
    valid_tree = TreeNode(10)
    for _ in range(20):
        valid_tree.insert(randint(0, 20))
    valid_tree.display()
    print(validate_bst(valid_tree))