# Check Balanced: Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree 
# such that the heights of the two subtrees of any node never differ by more 
# than one.
# Hints: #21, #33, #49, #105, #124


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
    
    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return float('-inf')
    
    return max(left_height, right_height) + 1


# -- Testing

from binary_search_tree import TreeNode
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
