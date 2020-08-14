# Minimal Tree: Given a sorted (increasing order) array with unique integer 
# elements, write an algorithm to create a binary search tree with minimal 
# height.
# Hints: #79, #73, #116


# -- Solution

from binary_search_tree import TreeNode


def minimal_tree(vals):
    """
    Creates a binary search tree with minimal
    height given an array of sorted integers
    """
    if not vals:
        return None
    
    n = len(vals)
    root = TreeNode(vals[n // 2])
    root.left = minimal_tree(vals[0: n//2])
    root.right = minimal_tree(vals[n // 2 + 1:])
    return root


# -- Testing

from random import sample

if __name__ == "__main__":
    vals = sample(range(0, 100), 20)
    vals.sort()
    tree = minimal_tree(vals)
    tree.display()
