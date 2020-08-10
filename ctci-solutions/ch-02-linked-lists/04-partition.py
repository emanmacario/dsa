# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24


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


def partition(head, x):
    pass


if __name__ == "__main__":
    head = ListNode.from_list([3, 5, 8, 5, 10, 2, 1])
    x = 5
    print(head)
    partition(head, x)