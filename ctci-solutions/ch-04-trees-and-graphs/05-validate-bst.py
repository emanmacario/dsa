# Validate BST: Implement a function to check if a binary tree is a binary 
# search tree.
# Hints: #35, #57, #86, #113, #128


# -- Solution

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
    

# -- Testing

from binary_search_tree import TreeNode
from random import randint


if __name__ == "__main__":
    invalid_tree = TreeNode(4, TreeNode(5), TreeNode(6))
    invalid_tree.display()
    print(validate_bst(invalid_tree))
    print('-' * 25)
    valid_tree = TreeNode(10)
    for _ in range(20):
        valid_tree.insert(randint(0, 20))
    valid_tree.display()
    print(validate_bst(valid_tree))