A = [[1, 2, 3, 4],
     [4, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
m = len(A)
n = len(A[0])
sec_diagonal_sum = 0
for i in range(m):
    for j in range(n):
        # row == numberOfColumn-column-1 is diagonal position
        if i == n-j-1:
            sec_diagonal_sum += A[i][j]

print(sec_diagonal_sum)