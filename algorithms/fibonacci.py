"""
Fibonacci Sequence:
    F(0) = 0, F(1) = 1, F(2) = 1 etc.

    0, 1, 1, 2, 3, 5, 8, 13, 21 etc.
"""

def fibonacci(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    
    return f_minus_1


if __name__ == '__main__':
    print(fibonacci(6))
