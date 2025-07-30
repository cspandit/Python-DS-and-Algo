"""Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer.
 He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
of the elements in the nxn submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in
the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

Solution to the problem lies in max of all the possible mirror elements as brute force method of reversing all rows
and column and looking for max sum will not be very ideal solution given that matrix size is very big
Below are the group of mirror elements in provided matrix :
mirror1 = [r0c0, r0c3, r3c0, r3c3]
mirror2 = [r0c1, r0c2, r3c1, r3c2]
mirror3 = [r1c1, r1c3, r2c0, r2c3]
mirror4 = [r1c1, r1c2, r2c1, r2c2]

Answer = sum(max(mirror1), max(mirror2), max(mirror3), max(mirror4))
"""
def flipping_matrix(matrix):
    n = len(matrix)//2
    summ = 0
    for i in range(n):
        for j in range(n):
            sm1  = matrix[i][j]
            sm2 = matrix[i][2*n-j-1]
            sm3 = matrix[2*n-i-1][j]
            sm4 = matrix[2*n-i-1][2*n-j-1]
            sm5 = max([sm1,sm2,sm3,sm4])
            summ += sm5
    return summ

matrix = [[112,42,83,119],
           [56,125,56,49],
           [15,78,101,43],
           [62,98,114,108]]

print(flipping_matrix(matrix))

