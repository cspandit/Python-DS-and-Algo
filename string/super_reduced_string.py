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

print(superReducedString('aaabccddd'))