# List of Depths: Given a binary tree, design an algorithm which creates a 
# linked list of all the nodes at each depth (e.g., if you have a tree with 
# depth D, you'll have D linked lists).
# Hints: #107, #123, #135


# -- Auxiliary data structures

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Returns a string representation of the linked list
        s = ''
        tmp = self
        while tmp:
            s += f"{tmp.val}->"
            tmp = tmp.next
        s += 'NULL'
        return s

    @classmethod
    def from_list(cls, vals):
        # Creates a linked list given a list of values
        if not vals:
            return None
        nodes = [ListNode(val) for val in vals]
        for n1, n2 in zip(nodes, nodes[1:] + [None]):
            n1.next = n2
        return nodes[0]


# -- Solution

def list_of_depths(root):
    """
    Creates a linked list for each depth level in a binary search tree
    """
    if not root:
        return

    lists = []
    queue = [root]
    while queue:
        depth = queue
        queue = [c for p in queue for c in [p.left, p.right] if c]
        # NB: In real interview, generate lists properly with dummy heads
        depth_list = ListNode.from_list([n.val for n in depth])
        lists.append(depth_list)

    return lists


# -- Testing

from binary_search_tree import TreeNode
from random import randint


if __name__ == "__main__":
    tree = TreeNode(10)
    for _ in range(20):
        tree.insert(randint(0, 20))
    tree.display()

    print('\n' + '-' * 25)
    lists = list_of_depths(tree)
    for depth in lists:
        print(depth)
