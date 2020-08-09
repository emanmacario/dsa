from pprint import pprint


def transpose_matrix(matrix):
    return list(zip(*matrix))


if __name__ == "__main__":
    matrix = [[3, 0, 8, 4],
              [2, 4, 5, 7],
              [9, 2, 6, 3],
              [0, 3, 1, 0]]

    transpose = transpose_matrix(matrix)

    pprint(f"Original: {matrix}")
    pprint(f"Transpose: {transpose}")
