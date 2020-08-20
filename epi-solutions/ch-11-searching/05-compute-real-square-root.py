# Square root computations can be implemented using sophisticated numerical 
# techniques involving iterative methods and logarithms. However, if you were 
# asked to implement a square root function, you would not be expected to know 
# these techniques.

# Implement a function which takes as input a floating point value and returns 
# its square root.


# -- Solution

import math

def square_root(n):
    """
    Perform binary search on the interval [n, 1.0] or [1.0, n] (depending
    on whether n >= 1). The prior interval accounts for input numbers that are
    less than 1. For example, the square root of 0.25 is 0.5.
    
    Time complexity is O(log n) and space complexity is O(1).
    """
    L, R = (n, 1.0) if n < 1 else (1.0, n)

    while not math.isclose(L, R):
        M = (L + R) / 2
        if M ** 2 < n:
            L = M
        else:
            R = M

    return L


# -- Testing

import math
import random

if __name__ == '__main__':
    n = random.uniform(0.0, 100.0)
    print(f'n: {n}')
    print(f'Estimated square: {square_root(n)}')
    print(f'Actual square:    {math.sqrt(n)}')