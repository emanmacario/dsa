# Paths with Sum: You are given a binary tree in which each node contains an 
# integer value (which might be positive or negative). Design an algorithm to 
# count the number of paths that sum to a given value. The path does not need 
# to start or end at the root or a leaf, but it must go downwards (traveling 
# only from parent nodes to child nodes).
# Hints: #6, #14, #52, #68, #77, #87, #94, #103, #108, #115


# -- Solution

def paths_with_sum(root, target):
    """
    Solution is O(NH), since we traverse H layers of the tree, and
    we process up to N nodes for each layer. If the tree is balanced,
    then time complexity is O(N log N) and stack space complexity is 
    O(log N). Note this has not been checked for correctness (but I'm
    pretty sure it is correct)
    """
    if not root:
        return 0

    return (paths_with_sum(root.left, target) + 
            paths_with_sum(root.right, target) + 
            pws_helper(root, 0, target))


def pws_helper(node, curr, target):
    if not node:
        return 0
    
    curr += node.val
    return (1 if curr == target else 0 +
            pws_helper(node.left, curr, target) +
            pws_helper(node.right, curr, target))


# -- Testing

from binary_search_tree import TreeNode
from random import randint, seed


if __name__ == "__main__":
    tree = TreeNode(5)
    for _ in range(25):
        tree.insert(randint(0, 20))
    tree.display()

    target = 38
    total_paths = paths_with_sum(tree, target)
    print(f'\nPaths with sum {target}: {total_paths} path(s)')
