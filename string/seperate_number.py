# String is beautiful when it can be separated with difference of 1

def separate_number(s):
    n = len(s)
    if n == 1 or s[0] == 0:
        return 'NO'
    mid = n//2
    i = 0
    while i < mid:
        temp = initial = s[:i+1]
        step = int(temp)
        while len(temp) < n:
            temp += str(step+1)
            step += 1

        if temp == s:
            return 'YES', initial
        else:
            i += 1
    return 'NO'



s = '13'
print(separate_number(s))

# ['1234', '91011', '99100']