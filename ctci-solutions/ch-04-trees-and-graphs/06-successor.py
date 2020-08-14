# Successor: Write an algorithm to find the "next" node (i.e., in-order 
# successor) of a given node in a binary search tree. You may assume that 
# each node has a link to its parent.
# Hints: #79, #91


from binary_search_tree import TreeNode

# Definition for a modified binary search tree node (includes parent pointer)
class ModifiedTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None, parent=None):
        super().__init__(val, left, right)
        self.parent = parent

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if not self.right:
                self.right = ModifiedTreeNode(val, parent=self)
            else:
                self.right.insert(val)
        else:
            if not self.left:
                self.left = ModifiedTreeNode(val, parent=self)
            else:
                self.left.insert(val)


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
    tree = ModifiedTreeNode(50)
    for _ in range(20):
        tree.insert(randint(25, 75))
    tree.display()

    print('---\nIn-order traversal:')
    in_order_traversal(tree)
    print('---')
    node = tree.search(35)
    print(f'Node: {node}')
    print(f'Successor: {in_order_successor(node)}')
    