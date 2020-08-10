# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f
# Hints: #72


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ''
        tmp = self
        while tmp:
            s += f"{tmp.val}->"
            tmp = tmp.next
        s += 'NULL'
        return s

    @classmethod
    def from_list(cls, vals):
        if not vals:
            return None
        nodes = [ListNode(val) for val in vals]
        for n1, n2 in zip(nodes, nodes[1:] + [None]):
            n1.next = n2
        return nodes[0]


def delete_middle_node(node):
    prev, curr = node, node.next
    while curr.next:
        prev.val = curr.val
        prev, curr = prev.next, curr.next

    prev.val = curr.val  # Don't forget to set the last node value!
    prev.next = None


if __name__ == "__main__":
    # Create linked list
    vals = list('abcdef')
    head = ListNode.from_list(vals)
    print(head)

    # Get 'middle' node
    tmp = head
    while tmp.val != 'b':
        tmp = tmp.next
    print(tmp)

    # Delete 'middle' node and print result
    delete_middle_node(tmp)
    print(head)

