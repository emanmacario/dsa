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

# TODO: Check correctness
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
    l5 = ListNode(4)
    l4 = ListNode(4, l5)
    l3 = ListNode(2, l4)
    l2 = ListNode(2, l3)
    head = ListNode(1, l2)

    print(head)
    remove_dups(head)
    print(head)