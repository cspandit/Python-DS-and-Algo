def quick_sort(array, low, high):
    if low < high:
        p_index = partition(array, low, high)
        quick_sort(array, low, p_index)
        quick_sort(array, p_index+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    p_index = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    arr[p_index], arr[high] = arr[high], arr[p_index]
    return p_index


A = [10, 16, 8, 12, 15, 6, 3, 9, 5]
quick_sort(A, 0, len(A)-1)
print(A)
