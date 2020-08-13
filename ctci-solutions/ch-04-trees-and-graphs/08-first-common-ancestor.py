# First Common Ancestor: Design an algorithm and write code to find the first 
# common ancestor of two nodes in a binary tree. Avoid storing additional nodes 
# in a data structure. NOTE: This is not necessarily a binary search tree.
# Hints: #70, #76, #28, #36, #46, #70, #80, #96


# From EPI:
# Any two nodes in a binary tree have a common ancestor, namely the root. The 
# lowest common ancestor (LCA) of any two nodes in a binary tree is the node 
# furthest from the root that is an ancestor of both nodes


# -- Solution

from . import TreeNode
from collections import namedtuple


def lca(tree, node0, node1):
    """
    The algorithm is structurally similar to a recursive postorder traversal, 
    and the complexities are the same. Specifically, the time complexity and 
    space complexity are O(N) and O(H), respectively, where H is the height of 
    the tree
    """
    Status = namedtuple('Status', ('num_target_nodes', 'ancestor'))
    
    def lca_helper(tree, node0, node1):
        """
        Returns an object consisting of an int and a node. The int field is 0,
        1, or 2 depending on how nany of {node0, node1} are present in tree. If
        both are present in tree, when ancestor is assigned to a non-null value,
        it is the LCA
        """
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in left subtree
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in right subtree
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes 
            + int(tree is node0) + int(tree is node1))

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


# -- Testing

from random import randint, seed

if __name__ == "__main__":
    seed(69)
    tree = TreeNode(50)
    for _ in range(25):
        tree.insert(randint(0, 100))
    tree.display()
    
    print('---')
    node0, node1 = tree.search(41), tree.search(44)
    print(f'Nodes: {node0} {node1}')
    print(f'LCA: {lca(tree, node0, node1)}')
