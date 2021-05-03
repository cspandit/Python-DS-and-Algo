from collections import defaultdict


def max_toys(string, n, k):
    start = 0
    end = 0
    max_no_of_toys = 0
    d = defaultdict(int)

    while end < n:
        d[string[end]] += 1

        if len(d) < k:
            end += 1

        elif len(d) == k:
            # print(sum(d.values()))
            max_no_of_toys = max(max_no_of_toys, sum(d.values()))
            end += 1

        else:
            while len(d) > k:
                d[string[start]] -= 1
                if d[string[start]] == 0:
                    d.pop(string[start])
                start += 1
            end += 1

    return max_no_of_toys


s = "abacbaba"
print(max_toys(s, len(s), 2))

