# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: #51, #100

def rotate_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            pass

    return matrix



if __name__ == "__main__":
    matrix = [[1, 2],
              [3, 4]]
    rotated = rotate_matrix(matrix)
    print(rotated)
