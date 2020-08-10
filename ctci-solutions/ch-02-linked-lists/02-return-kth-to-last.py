# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# Hints: #8, #25, #41, #67, #126


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


def return_kth_to_last(head, k):
    """
    Solution is O(N) time complexity.
    Note this algorithm assumes at least k nodes in the list
    :param head: head of linked-list
    :param k: k value
    :return: value of k-th last element of singly-linked list
    """
    slow = fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow, fast = slow.next, fast.next

    return slow.val


if __name__ == "__main__":
    head = ListNode.from_list([1, 2, 3, 4])
    print(return_kth_to_last(head, 3))
    print(return_kth_to_last(head.next, 2))
    print(return_kth_to_last(head.next.next, 1))
