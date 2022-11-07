from collections import defaultdict


def largest_sub_brute_force(s, n):
    max_sub = 0
    for i in range(n):
        d = defaultdict(int)
        for j in range(n):
            temp = s[i:j+1]
            for x in temp:
                d[x] += 1
            if len(d) == len(temp):
                max_sub = max(max_sub, len(d))
    return max_sub

def largest_sub(string, n):
    start = 0
    end = 0
    max_size = 0
    d = defaultdict(int)
    while end < n:
        d[string[end]] += 1

        if len(d) == (end - start + 1): # window size will be the condition to check
            max_size = max(max_size, (end - start + 1))
            end += 1
        else:
            while len(d) < (end - start + 1):
                d[string[start]] -= 1
                if d[string[start]] == 0:
                    d.pop(string[start])
                start += 1
            end += 1

    return max_size


s = "pwwkew"
n = len(s)
print(largest_sub(s, n))