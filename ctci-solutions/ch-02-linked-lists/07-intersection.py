# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
# Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129


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


def getIntersectionNode(headA, headB):
    """
    Returns intersection node if it exists, else None.
    Note that intersection is defined by equivalent object
    references, not equivalent values.

    Time complexity is O(A + B), space complexity is O(1)
    """
    # Get lengths of both linked lists, O(A + B)
    dh_A, dh_B = headA, headB
    lenA = lenB = 0
    while dh_A:
        lenA += 1
        dh_A = dh_A.next
        
    while dh_B:
        lenB += 1
        dh_B = dh_B.next
    
    # Compute length differences between lists
    diff = lenA - lenB
    if diff > 0:
        is_A_longer = True
    else:
        is_A_longer = False
    
    # Traverse the longer list by 'diff' nodes
    dh_A, dh_B = headA, headB
    for _ in range(abs(diff)):
        if is_A_longer:
            dh_A = dh_A.next
        else:
            dh_B = dh_B.next
    
    # Get the intersection node, if it exists
    while dh_A and dh_B:
        if dh_A is dh_B:
            return dh_A
        dh_A, dh_B = dh_A.next, dh_B.next


if __name__ == "__main__":
    headA = ListNode.from_list([1, 2, 3, 4])
    headB = headA.next.next.next
    print(headA)
    print(headB)

    intersection = getIntersectionNode(headA, headB)
    if intersection:
        print('-- Intersection found --')
        print(intersection)
    else:
        print('-- No intersection found --')
