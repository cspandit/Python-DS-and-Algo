# Given an array a[0 . . . n-1]. We should be able to efficiently find the GCD from index qs (query start) to qe
# (query end) where 0 <= qs <= qe <= n-1.
#
# Example :
#
# Input : a[] = {2, 3, 60, 90, 50};
# Index Ranges : {1, 3}, {2, 4}, {0, 2}
# Output: GCDs of given ranges are 3, 10, 1

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd_array(array, qs, qe):
    l = array[qs]
    r = array[qs+1]
    gcd = find_gcd(l, r)
    for j in range(2, qe+1):
        gcd = find_gcd(gcd, array[j])

    print(gcd)


arr = [2, 3, 60, 90, 50]
gcd_array(arr, 2, 4)