# Input:
# ar1[] = {1, 5, 10, 20, 40, 80}
# ar2[] = {6, 7, 20, 80, 100}
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20, 80

def intersection(array1, array2):
    output = []
    while array1 and array2:
        if array1[0] < array2[0]:
            array1.pop(0)
        elif array1[0] > array2[0]:
            array2.pop(0)
        else:
            output.append(array1.pop(0))
            array2.pop(0)
    return output


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]

print(intersection(intersection(A, B), C))

