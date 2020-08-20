# Write a program which takes a non-negative integer and returns the largest 
# integer whose square is less than or equal to the given integer. For example, 
# if the input is 16, return 4; if the input is 300, return 17, since 
# 17^2 = 289 < 300 and 18^2 = 324 > 300.


# -- Solution

def square_root(k):
    """
    Perform binary search on the interval [0, k] for the square.
    Time complexity is O(log k) and space complexity is O(1).
    """
    assert(k > -1)
    L, R, result = 0, k, 0

    while L <= R:
        M = (L + R) // 2
        if M ** 2 <= k:
            result = M
            L = M + 1
        else:
            R = M - 1

    return result


# -- Testing

from math import sqrt

def test_square_root(k):
    return square_root(k) == int(sqrt(k))

if __name__ == '__main__':
    k = 300
    print(f'k: {k}')
    print(f'Square: {square_root(k)}')

    tests = [test_square_root(k) for k in range(10_000)]
    print(all(tests))