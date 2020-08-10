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


def intersection(h1, h2):
    seen = set()
    while h1 or h2:
        if h1:
            if h1 in seen:
                return h1
            seen.add(h1)
            h1 = h1.next

        if h2:
            if h2 in seen:
                return h2
            seen.add(h2)
            h2 = h2.next

    return None


if __name__ == "__main__":
    h1 = ListNode.from_list([1, 2, 3, 4])
    h2 = h1.next.next.next
    print(h1)
    print(h2)

    intersect = intersection(h1, h2)
    if intersect:
        print('-- Intersection found --')
        print(intersect)
    else:
        print('-- No intersection found --')
