from collections import defaultdict


def largest_sub(string, k, n):
    start = 0
    end = 0
    max_size = 0
    d = defaultdict(int)

    while end < n:
        d[string[end]] += 1

        if len(d) < k:
            end += 1

        elif len(d) == k:
            max_size = max(max_size, end-start+1)
            end += 1

        else:
            while len(d) > k:
                d[string[start]] -= 1
                if d[string[start]] == 0:
                    d.pop(string[start])
                start += 1
            end += 1
    return max_size


s = "abbacebebebe"
n = len(s)
print(largest_sub(s, 3, n))