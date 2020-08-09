# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Hints: #17, #74, #702


def zero_matrix(matrix):
    zero_cols = set()
    zero_rows = set()

    total_rows = len(matrix)
    total_cols = len(matrix[0])

    for i in range(total_rows):
        for j in range(total_cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)


if __name__ == "__main__":
    zero_cols = set()
    zero_rows = set()
