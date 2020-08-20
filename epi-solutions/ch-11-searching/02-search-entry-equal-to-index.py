# Design an efficient algorithm that takes a sorted array of distinct integers, 
# and returns an index i such that the element at index i equals i. For example,
# when the input is A = <-2,0,2,3,6,7,9> your algorithm should return 2 or 3.


# -- Solution



def search_entry_equal_to_its_index(A):
    """
    Time complexity is O(log N), since the problem can be reduced down to 
    binary search. If A[j] > j, then no entry after j can satisfy the given 
    criterion. This is because each element in the array is at least 1 greater 
    than the previous element. For the same reason , if A[j] < j, no entry 
    before j can satisfy the given criterion.
    """
    L, R = 0, len(A) -1

    while L <= R:
        M = L + (R - L) // 2
        if A[M] > M:
            R = M - 1
        elif A[M] == M:
            return M
        else:
            # A[M] < M
            L = M + 1

    return -1

        
# -- Testing

from random import randint

if __name__ == '__main__':
    A = sorted(set(randint(-5, 10) for _ in range(15)))
    k = randint(-10, 10)
    print(f'A: {A}')
    print(f'Size: {len(A)}')
    print(search_entry_equal_to_its_index(A))