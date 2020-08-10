# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier]
# Output: C
# Hints: #50, #69, #83, #90


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


def loop_detection(head):
    """
    Algorithm Explanation:
    1. Proceed with usual 'runner' technique to detect loop
    2. The meeting point of two pointers is k-steps before the head of the loop (k is length of non-cyclic part)
    3. Move 'slow' to head of loop, while keeping 'fast' at collision point
    4. Both pointers are k-steps from start of loop
    5. Proceed both at same rate; both will meet at start of cycle

    NB: Assumes that 'head' is a circular linked list

    Solution is O(N) since loop detection is O(N), and finding start of list is O(K), where K < N
    """
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break

    slow = head
    while slow is not fast:
        slow, fast = slow.next, fast.next

    return slow


if __name__ == "__main__":
    # Create cyclic linked list:
    #       1 -> 2 -> 3 -> 4 -> 5 ->
    #                 |            |
    #                 -------------
    head = ListNode.from_list([1, 2, 3, 4, 5])
    print(head)
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head.next.next

    cycle_start = loop_detection(head)
    print(cycle_start.val)
