def changes(s):
    s = list(s)
    n = len(s)
    l = 0
    h = n-1
    count = 0
    while l < h:
        if s[l] != s[h]:
            count += 1

        # this is to make sure that always larger char is changed to lower char to maintain lexo order
        if s[h] > s[l]:
            s[h] = s[l]
        else:
            s[l] = s[h]
        l += 1
        h -= 1


    print("".join(s))
    print(count)

changes('geeks')