def find_union(array1, array2):
    union_output = []
    while array1 and array2:
        if array1[0] < array2[0]:
            temp = array1.pop(0)
            if temp not in union_output:
                union_output.append(temp)
        elif array1[0] > array2[0]:
            temp = array2.pop(0)
            if temp not in union_output:
                union_output.append(temp)
        else:
            temp = array1.pop(0)
            array2.pop(0)
            if temp not in union_output:
                union_output.append(temp)

    while array1:
        temp = array1.pop(0)
        if temp not in union_output:
            union_output.append(temp)
    while array2:
        temp = array2.pop(0)
        if temp not in union_output:
            union_output.append(temp)

    return union_output + array1 + array2

# in case of intersection append happens only when array1[0] is equal to array2[0]


A = [1, 1, 3, 4, 5, 7, 7]
B = [2, 3, 5, 6, 6]
print(find_union(A, B))