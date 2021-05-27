def multiply(A, B):
    m = len(A)
    n = len(B[0])
    C = [[0 for x in range(2)] for y in range(2)]

    for i in range(m):
        for j in range(n):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print(C)


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

multiply(A, B)