# BST Sequences: A binary search tree was created by traversing through an array 
# from left to right and inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could have led to this tree.
# EXAMPLE
# Input:
#     2
#    / \
#   1   3
# Output: {2, 1, 3}, {2, 3, 1}
# Hints: #39, #48, #66, #82


# -- Solution

from binary_search_tree import TreeNode


# TODO: This is fucked...

def bst_sequences(root):
    pass



# -- Testing

from random import randint, seed

if __name__ == "__main__":
    seed(100)
    tree = TreeNode(50)
    for _ in range(5):
        tree.insert(randint(0, 100))
    tree.display()
