def multiply(A, B):
    m = len(A)
    n = len(B[0])
    res = [[0 for x in range(n)] for y in range(n)]
    print(res)
    for i in range(m):
        for j in range(n):
            for k in range(len(B)):
                res[i][j] = res[i][j] + A[i][k]*B[k][j]
    print(res)

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]


multiply(A, B)