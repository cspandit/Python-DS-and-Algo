# Problem is to search an element in 2d sorted matrix in O(n):
# We can apply BS in this case. Lets assume upper right as mid element


def search(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    # lets say nXm is matrix dimension
    i = 0
    j = m-1
    while i < n and j >= 0:
        if matrix[i][j] == key:
            return i, j
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1
    return -1


A = [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]

print(search(A, 27))
