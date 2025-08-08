# remove both element at ith and (i+1)th position if they are same and new combination forming after that

def superReducedString(s):
    s_list = list(s)
    i = 0
    while i < len(s_list)-1:
        if s_list[i] == s_list[i+1]:
            del(s_list[i])
            del(s_list[i])
            i = 0
        else:
            i += 1

    if len(s_list) == 0:
        return 'Empty_String'
    else:
        return "".join(s_list)

#using dictionary
def superReducedString_chandra(s):
    res = ''
    d = dict.fromkeys(s, 0)
    for c in s:
        d[c] += 1
    for c in s:
        if d[c] % 2 != 0:
            res += c
            d[c] -= 1
    return res

#withoiut using dictionary extra list
def superReducedString_chandra_string(s):
    res = ''
    n = len(s)
    i = 0
    while i < n:
        if i == n-1:
            res += s[i]
            i += 1
        elif s[i] ==  s[i+1]:
            i += 2
        else:
            res += s[i]
            i += 1
    return res

print(superReducedString_chandra_string('aaabccddd'))