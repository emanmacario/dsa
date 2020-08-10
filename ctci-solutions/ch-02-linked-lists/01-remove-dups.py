# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints: #9, #40

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


def remove_dups(head):
    """
    Solution is O(N) in time and space, removing duplicates in place (hence, no return value)
    """
    # Edge cases: empty or one-element linked list
    if not head or not head.next:
        return

    # Traverse through the list, 'deleting' duplicate nodes
    seen = set()
    prev, curr = None, head
    while curr:
        if curr.val in seen:
            curr = curr.next
            prev.next = curr
            continue

        seen.add(curr.val)
        prev, curr = curr, curr.next


if __name__ == "__main__":
    head = ListNode.from_list([1, 2, 3, 4, 3, 4, 3])
    print(head)
    remove_dups(head)
    print(head)
