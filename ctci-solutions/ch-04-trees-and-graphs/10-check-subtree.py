# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger 
# than T2. Create an algorithm to determine if T2 is a subtree of T1. A tree T2 
# is a subtree of T1 if there exists a node n in T1 such that the subtree of n 
# is identical to T2. That is, if you cut off the tree at node n, the two trees 
# would be identical.
# Hints: #4, #11, #18, #31, #37


# -- Solution

from binary_search_tree import TreeNode


def check_subtree(T1, T2):
    """
    Checks if T2 is a subtree of T1. Solution is O(N + KM) where N and M
    are the total number of nodes in T1 and T2, and K is number of times T2's 
    root occurs in T1
    """
    # The empty tree is always a subtree
    if not T2:
        return True

    # Larger tree exhausted and subtree still not found
    if not T1:
        return False

    # Check if trees are equal
    if is_equal(T1, T2):
        return True

    # Check if subtree is a subtree of larger tree
    return check_subtree(T1.left, T2) or check_subtree(T1.right, T2)


def is_equal(T1, T2):
    """
    Checks if two trees are equal with respect to structure and values
    """
    # Both empty
    if not T1 and not T2:
        return True

    # One empty
    if not T1 or not T2:
        return False

    # Non-equal values
    if T1.val != T2.val:
        return False

    # Otherwise, check that subtrees are equivalent
    return is_equal(T1.left, T2.left) and is_equal(T1.right, T2.right)


# -- Testing

from random import randint, seed

if __name__ == "__main__":
    seed(1209)
    T1 = TreeNode(50)
    for _ in range(50):
        T1.insert(randint(0, 100))
    T1.display()


    T2 = T1.search(42)
    T2.display()

    print(check_subtree(T1, T2))

