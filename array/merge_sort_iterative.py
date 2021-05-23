def merge_sort(arr):
    n = len(arr)
    size = 1
    ps = 1
    while size < n:

        merge_pass(arr, size, n)
        print("This is after pass {}: ".format(ps), arr)
        size = size*2
        ps = ps+1


def merge_pass(arr, size, n):
    l1 = 0

    while(l1+size<n):
        r1 = l1+size-1
        l2 = l1+size
        r2 = l2+size-1

        if r2 >= n:
            r2 = n-1

        merge(arr, l1, r1, l2, r2)

        l1 = r2+1


def merge(arr, l1, r1, l2, r2):
    arr1 = arr[l1:r1+1]
    arr2 = arr[l2:r2+1]
    i,j,k = 0,0,l1

    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1

        else:
            arr[k] = arr2[j]
            j += 1

        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1


arr = [13, 5, 12, 11, 6, 7]
merge_sort(arr)
print(arr)

