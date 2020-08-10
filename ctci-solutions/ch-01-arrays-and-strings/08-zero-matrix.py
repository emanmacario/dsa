# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Hints: #17, #74, #702


def zero_matrix(matrix):
    """
    Solution is O(MN) time complexity since we touch each element at least once
    It is O(M + N) space complexity since since we store the zero row and zero column indexes

    Additional:
        - To make algorithm O(1) space, use first row and column of matrix as storage
          for zero rows and columns (i.e. no need to use additional data structures)
        - But, need to nullify the first row and column after all other rows and columns
          (if necessary)

    """
    zero_rows = set()
    zero_cols = set()

    total_rows = len(matrix)
    total_cols = len(matrix[0])

    for i in range(total_rows):
        for j in range(total_cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for row_index in zero_rows:
        nullify_row(matrix, row_index)

    for col_index in zero_cols:
        nullify_col(matrix, col_index)


def nullify_row(matrix, row_index):
    row = matrix[row_index]
    for i in range(len(row)):
        row[i] = 0


def nullify_col(matrix, col_index):
    for i in range(len(matrix)):
        matrix[i][col_index] = 0


if __name__ == "__main__":
    matrix = [[1, 2, 3, 0],
              [0, 5, 1, 3],
              [1, 1, 1, 1]]

    for r in matrix:
        print(*r)

    zero_matrix(matrix)

    print('---')
    for r in matrix:
        print(*r)
