# An array is said to be cyclically sorted if it is possible to cyclically shift 
# its entries so that it becomes sorted.

# Design an O(log N) algorithm for finding the position of the smallest element 
# in a cyclically sorted array. Assume all elements are distinct. For example, 
# for the array <378, 478, 550, 631, 103, 203, 220, 234, 279, 358> your 
# algorithm should return 4.

# Hint: Use the divide and conquer principle.


# -- Solution

def search_smallest(A):
    """
    Effectively, we are finding the rotation point. The time complexity 
    is O(log N). We use binary search to converge to the smallest index, 
    by comparing the 'middle' value with the 'right' value on each iteration, 
    and reducing the search space accordingly.
    """
    L, R = 0, len(A) - 1
    
    while L <= R:
        M = (L + R) // 2
        if A[M] < A[R]:
            R = M
        else:
            L = M + 1
        
    return L - 1



# -- Testing

from random import randint

if __name__ == '__main__':
    sorted_A = sorted(set(randint(0, 20) for _ in range(8)))
    r = randint(1, len(sorted_A))
    cyclic_A = sorted_A[r:] + sorted_A[:r]
    print('Cyclic A: ' + ''.join(f'{n:3} ' for n in cyclic_A))
    print('Indexes : ' + ''.join(f'{i:3} ' for i in range(len(cyclic_A))))
    print(f'---\nSmallest: {search_smallest(cyclic_A):3}')
    
