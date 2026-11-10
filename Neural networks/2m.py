import math

def matrix_multiply(A, B):
    """Multiply two matrices A and B without using numpy"""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    print(result)


matrix_multiply([[1,2],[3,4]],[[5,6],[7,8]])