from bisect import bisect_left
from random import randint


def binary_search(a, v, lo=0, hi=None):
    """
    Binary search utilising Python 3 standard libraries
    """
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, v, lo, hi)
    return pos if pos != hi and a[pos] == v else -1


def binary_search(A, v, low, high):
    """
    Traditional recursive binary search
    """
    if low > high:
        return -1

    mid = (low + high) // 2
    if v == A[mid]:
        return mid
    elif v < A[mid]:
        return binary_search(A, v, low, mid - 1)
    else:
        return binary_search(A, v, mid + 1, high)


def binary_search(A, target):
    """
    Traditional iterative binary search (accounting for integer overflow)
    """
    L, R = 0, len(A) - 1
    while L <= R:
        M = L + (R - L) // 2  # Avoids integer overflow (unnecessary in Python)
        if A[M] < target:
            L = M + 1
        elif A[M] == target:
            return M
        else:
            R = M - 1
    
    return -1
            


if __name__ == '__main__':
    v = randint(0, 20)
    A = sorted([randint(0, 20) for _ in range(10)])
    print(f'Target: {v:3}')
    print(f'Array:  {A}')
    index = binary_search(A, v, 0, len(A) - 1)
    print(f'Index: {index}')
    print(f'Target in Array: {v in A}')
    print(f'Correctness: {((v in A and A[index] == v) or index == -1)}')
