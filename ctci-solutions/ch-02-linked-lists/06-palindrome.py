# Palindrome: Implement a function to check if a linked list is a palindrome.
# Hints: #5, #13, #29, #61, #101


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


def palindrome(lst):
    pass


if __name__ == "__main__":

    head = ListNode.from_list([1, 2, 3, 2, 1])
    print(f"ORIGINAL: {head}")
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(f"MIDPOINT: {slow}")
    # print(fast)