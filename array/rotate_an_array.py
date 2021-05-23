def rotate(arr, k):
    for i in range(k):
        temp = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]

        arr[-1] = temp


A = [1, 2, 3, 4, 5, 6]
rotate(A, 2)
print(A)