def alternate(s):
    n = len(s)
    #s = list(s)
    i = 0
    count = 0
    while i < n-1:
        if s[i] == s[i+1]:
            count += 1
            i += 1
        else:
            i += 1
    return count
s = 'AABAAB'
print(alternate(s))