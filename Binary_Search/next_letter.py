# Problem is to find the next letter for given in a sorted alphabetical array
# This problem is identical to finding ceil of given number in sorted array. Only difference is we return number if
# found in array but here we dont.


def next_letter(array, key):
    low = 0
    high = len(array)-1
    nex = ""
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            low = mid + 1

        elif array[mid] > key:
            nex = max(nex, array[mid])
            high = mid - 1

        else:
            low = mid + 1

    return nex


A = ['a', 'c', 'f', 'h']
nex_let = next_letter(A, 'e')
print(nex_let)