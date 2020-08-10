# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: #51, #100


def rotate(matrix):
    """
    Solution is O(N^2) time complexity. Idea is to implement
    rotation in 'layers', starting from outermost and working
    our way into the middle layers of the matrix. This swaps
    elements in-place
    """
    # Assert N x N matrix structure
    assert(matrix and all(l == len(matrix) for l in [len(r) for r in matrix]))

    N = len(matrix)
    layers = N // 2

    for layer in range(layers):
        first = layer
        last = N - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # Save top

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return matrix


def rotate2(matrix):
    """
    My own one-liner solution that is O(N^2) (but not in-place)
        - Since zipping is O(N^2) b/c we touch all elements
        - Reversing is O(N^2) since we reverse N lists and each reverse is O(N)
        - i.e. Reversing a list is O(N) in Python
    """
    # Assert N x N matrix structure
    assert (matrix and all(l == len(matrix) for l in [len(r) for r in matrix]))

    return [list(row)[::-1] for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [5, 6, 7],
              [9, 10, 11, 12],
              [13, 14, 15]]
    for row in matrix:
        print(row)
    rotated = rotate(matrix)
    print('---')
    for row in rotated:
        print(row)
