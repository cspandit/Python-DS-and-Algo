from collections import defaultdict


def count_dup(string):
    d = defaultdict(int)
    for c in string:
        d[c] += 1

    for k, v in d.items():
        if v > 1:
            print((k, v))


count_dup('chandra')
