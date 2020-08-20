# Write a method that takes a sorted array and a key and returs the index of the first occurrence of
# that key in the array. Return -1 if the key does not appear in the array. For example, when applied
# to the array in Figure 11.1 your algorithm should return 3 if the given key is 108; if it is 285, your
# algorithm should return 6.

# Hint: What happens when every entry equals k? Don't stop when you first see k.


# -- Solution

def search_first_of_k(A, k):
    """
    Time complexity is O(log N). Each 
    iteration reduces size of search 
    space by half
    """
    L, R, result = 0, len(A) - 1, -1

    while L <= R:
        M = (L + R) // 2
        if A[M] < k:
            L = M + 1
        elif A[M] == k:
            result = M
            R = M - 1
        else:
            R = M - 1

    return result


# -- Testing

from random import randint

if __name__ == '__main__':
    A = sorted(randint(-10, 10) for _ in range(10))
    k = randint(-10, 10)
    print(f'A: {A}')
    print(f'N: {len(A)}')
    print(f'k: {k}')
    print(search_first_of_k(A, k))