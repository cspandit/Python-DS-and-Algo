# if odd number of characters in a string more than one then it cannot form palindrome


def palindrome_funny(s):
    d = dict.fromkeys(s, 0)
    for x in s:
        d[x] += 1
    count = 0
    for i in d.values():
        if i%2 != 0:
            count += 1
        if count > 1:
            return False
    return True


def palindrome(s):
    l = 0
    h = len(s)-1
    while l< h:
        if s[l] != s[h]:
            return False
        l += 1
        h -= 1
    return True


s = "malayalam"
print(palindrome(s))
