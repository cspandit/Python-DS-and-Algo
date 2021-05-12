# problem is two find the min size window in string 1 will contain all the characters for string 2


from collections import defaultdict
from sys import maxsize


def min_window(string1, string2):
    d = defaultdict(int)
    for s in string2:
        d[s] += 1

    n = len(string1)
    start = 0
    end = 0
    mn = maxsize
    count = len(d)

    while end < n:
        d[string1[end]] -= 1
        if d[string1[end]] == 0:
            count -= 1

        if count == 0:
            while count == 0:
                mn = min(mn, end - start + 1)
                d[string1[start]] += 1
                if d[string1[start]] == 1:
                    count += 1
                start += 1
        end += 1
    return mn


s1 = "geeksgforgeeks"
s2 = "gks"
print(min_window(s1, s2))
