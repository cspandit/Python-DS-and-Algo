def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break
    return arr


def bubble_sort_recur(arr, n=None):
    if n is None:
        n = len(arr)
    count = 0
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
    if count == 0:
        return arr
    return bubble_sort_recur(arr, n-1)


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort_recur(arr))