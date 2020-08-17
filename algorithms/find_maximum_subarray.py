from itertools import accumulate


def find_maximum_subarray(A, debug=False):
    """
    Time complexity is O(N), space complexity is O(1). The maximum subarray sum 
    with subarray ending at index j is equal to S[j] - min(S[k]) 
    where k <= j, and S[i] = sum(A[0..i]) (including element at index i)

    This variant of the algorithm allows for empty subarrays, meaning
    that it will return zero if the input contains no positive elements
    (including when the input is empty)
    """
    if debug:
        print(f'Input: {A}\n' + '-' * 50)

    min_sum = max_sum = 0
    
    for running_sum in accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
        if debug:
            print(f'Running: {running_sum:3}  Min: {min_sum:3}  Max: {max_sum:3}')

    return max_sum


def kadanes_algorithm(A):
    """
    Find the largest sum of any contiguous subarray, in O(N) time
    and O(1) space. Allows for empty subarrays

    For problem variants that do not allow empty subarrays, we can set
    global max and current max to the first array element, and iterate
    through A[1..N-1]. This is what I did in the LeetCode question for
    this problem
    """
    best_sum = float('-inf')
    current_sum = 0
    for n in A:
        current_sum = max(0, current_sum + n)
        best_sum = max(best_sum, current_sum)

    return best_sum


# -- Testing

from random import randint

if __name__ == "__main__":
    A = [randint(-10, 10) for _ in range(10)]
    # A = [-1, -2, -3]
    max_sum = find_maximum_subarray(A, debug=True)