# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 - > 1 -> 2. That is, 912.
# Hints: #7, #30, #71, #95, #109


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


def sum_lists(l1, l2):
    total = sum_list(l1) + sum_list(l2)
    dummy_head = tail = ListNode()
    vals = str(total)[::-1]
    for val in map(int, vals):
        node = ListNode(val)
        tail.next = node
        tail = tail.next

    return dummy_head.next


def sum_list(l):
    """
    Computes sum for a single linked list
    E.g. (6 -> 1 -> 7) gives 716
    """
    total = 0  # Cumulative sum
    n = 0      # Current power
    while l:
        total += l.val * pow(10, n)
        l = l.next
        n += 1
    return total


if __name__ == "__main__":
    l1 = ListNode.from_list([7, 1, 6])
    l2 = ListNode.from_list([5, 9, 2])
    print(sum_lists(l1, l2))
