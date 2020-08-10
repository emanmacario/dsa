# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# Hints: #8, #25, #41, #67, #126


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

# TODO: Check correctness
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
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    print(l1)

    print(return_kth_to_last(l1, 3))
    print(return_kth_to_last(l2, 2))
    print(return_kth_to_last(l3, 1))
