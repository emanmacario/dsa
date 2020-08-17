# Magic Index: A magic index in an array A[0...n-1] is defined to be an 
# index such that A[i] = i. Given a sorted array of distinct integers, write a 
# method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?
# Hints: #170, #204, #240, #286, #340


# -- Solution for original question

def magic_index(A):
    """
    Returns the 'magic index' of A (if it exists).
    Uses the properties of the sorted array of distinct integers
    in addition to binary search to run in O(log N) time
    """
    def binary_search_magic_index(A, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2

        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            return binary_search_magic_index(A, low, mid - 1)
        else:
            return binary_search_magic_index(A, mid + 1, high)

    return binary_search_magic_index(A, 0, len(A) - 1)


# -- Solution for follow up question

def magic_index_duplicates(A):
    """
    Returns the magic index of A (if it exists). Allows
    for duplicate values in the input array. Solution is
    still O(log N), however we may need to recurse on both
    left and right subarrays
    """
    def binary_search_magic_index_duplicates(A, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if A[mid] == mid:
            return mid

        # Now, magic index could be on either side of the mid point
        # However, we can prune the left and right subarrays to quicken
        # search, because we know that it is impossible for the magic
        # index to be at certain indexes

        # Search left
        left_high = min(A[mid], mid - 1)
        left = binary_search_magic_index_duplicates(A, low, left_high)
        if left > -1:
            return left

        # Search right
        right_low = max(A[mid], mid + 1)
        right = binary_search_magic_index_duplicates(A, right_low, high)

        return right

    return binary_search_magic_index_duplicates(A, 0, len(A) - 1)

        
# -- Testing

from random import randint


def test_magic_index():
    A = sorted(set(randint(-10, 10) for _ in range(randint(5, 10))))
    print('A[i]: ' + ''.join(f'{num:4}' for num in A))
    print('   i: ' + ''.join(f'{i:4}' for i in range(len(A))))
    print('-' * 50)
    print(f'Magic Index: {magic_index(A)}')


def test_magic_index_duplicates():
    A = sorted(randint(-10, 10) for _ in range(randint(5, 10)))
    print('A[i]: ' + ''.join(f'{num:4}' for num in A))
    print('   i: ' + ''.join(f'{i:4}' for i in range(len(A))))
    print('-' * 50)
    print(f'Magic Index: {magic_index_duplicates(A)}')


if __name__ == '__main__':
    test_magic_index_duplicates()



