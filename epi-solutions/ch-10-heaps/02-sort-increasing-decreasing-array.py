# An array is said to be k-increasing-decreasing if elements repeatedly increase 
# up to a certain index after which they decrease, then again increase, a total 
# of k times.

# For example (k = 4):
# 57 131 493 | 294 221 | 339 418 452 | 442 190

# Design an efficient algorithm for sorting a k-increasing-decreasing array.

# Hint: Can you cast this in terms of combining k sorted arrays?


# -- Solution

# Upper bound is O(N log N)

def sort_k_increasing_decreasing_array(A):
    """
    Solution is to extract and merge k sorted arrays from the input array.
    Hence, time complexity is O(N), whereas sorting is O(N log N).
    """
    pass



# -- Testing

if __name__ == '__main__':
    A = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]