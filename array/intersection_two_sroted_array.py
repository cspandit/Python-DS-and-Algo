def intersection(arr1, arr2):
    res = []
    while arr1 and arr1:
        if arr1[-1] == arr2[-1]:
            res.append(arr1[-1])
            arr1.pop()
            arr2.pop()
        elif arr1[-1] < arr2[-1]:
            arr1.pop()
        else:
            arr2.pop()
    return res


list1 = [6, 5, 4, 3, 2, 1]
list2 = [8, 6, 4, 2]

print(intersection(list1, list2))