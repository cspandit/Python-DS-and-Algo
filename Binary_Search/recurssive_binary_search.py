def search(arr, l, h, key):
    if l > h:
        return
    mid = l + (h-l)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return search(arr, l, mid-1, key)
    else:
        return search(arr, mid+1, h, key)


A = [1, 2, 3, 4, 5, 6, 7, 8]
print(search(A, 0, len(A)-1, 5))
