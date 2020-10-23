# Palindrome: Implement a function to check if a linked list is a palindrome.
# Hints: #5, #13, #29, #61, #101


# Definition for singly-linked list
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


def palindrome(head):
    """
    Solution has O(N) time complexity. Idea is to
    reverse the second half of the list, then compare
    it with the first half
    """
    # Edge cases: empty list or single element list
    if not head or not head.next:
        return True

    # Use 'runner' technique to get middle node
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Reverse the second half of the list
    reverse_slow = reverse_list(slow)

    print('HEAD:', head)
    print('REVERSE SLOW:', reverse_slow)

    # Compare first half with reversed second half2
    while head and reverse_slow:
        if head.val != reverse_slow.val:
            return False
        head, reverse_slow = head.next, reverse_slow.next

    return True


def reverse_list(head):
    prev, curr = None, head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


if __name__ == "__main__":
    head = ListNode.from_list([1, 2, 2, 1]) # ListNode.from_list([1, 2, 3, 4, 3, 2, 1])
    print(head)
    print(palindrome(head))
