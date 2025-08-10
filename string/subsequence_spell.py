# We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber
# that a subsequence maintains the order of characters selected from a sequence.

def maintained_order(s):
    order = 'hackerrank'
    i = 0
    res = ''
    for c in s:
        if c == order[i]:
            res += c
            i += 1
            if i >= len(order):
                break
    if res == order:
        return 'YES'
    else:
        return 'NO'


s = 'ahaacckkerrannnkkk'
print(maintained_order(s))