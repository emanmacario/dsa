# Call a 2D array sorted if its rows and its columns are nondecreasing. 
# For example:
#   -1  2  4  4  6
#    1  5  5  9 21
#    3  6  6  9 22
#    3  6  8 10 24
#    6  8  9 12 25
#    8 10 12 13 40

# Design an algorithm that takes a 2D sorted array and a number and checks 
# whether that number appears in the array. For example, if the input is the 
# 2D sorted array in the example and the number is 7, your algorithm should 
# return false; if the number is 8, your algorithm should return true.

# Hint: Can you eliminate a row or a column per comparison?


# -- Solution

def matrix_search(A, x):
    """
    Idea is to start at top right corner of matrix,
    and eliminate columns or rows that cannot contain x,
    iteratively.

    This is effectively a unique path starting from the top
    right of the matrix, moving only down or left, to either 
    the element (if it exists), or to one unit outside of 
    the left or bottom edge of the matrix.

    Hence, time complexity is O(M + N), where M is total rows 
    and N is total columns.
    """
    # Sanity check
    assert(A and A[0])

    # Perform search
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if x == A[row][col]:
            # Target found
            return True
        elif A[row][col] > x:
            # Matrix value larger than target, move left
            col -= 1
        else:
            # Matrix value smaller than target, move down
            row += 1

    return False
    

# -- Testing

from pprint import pprint

if __name__ == '__main__':
    A = [[-1, 2, 4, 4, 6],
        [1, 5, 5, 9, 21],
        [3, 6, 6, 9, 22],
        [3, 6, 8, 10, 24],
        [6, 8, 9, 12, 25],
        [8, 10, 12, 13, 40]]

    pprint(A)
    print(matrix_search(A, 8))  # True
    print(matrix_search(A, 7))  # False
