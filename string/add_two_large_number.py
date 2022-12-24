def find_sum(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 < n2:
        n_s = n1
        n_l = n2
        s_s = s1[::-1]
        s_l = s2[::-1]
    else:
        n_s = n2
        n_l = n1
        s_s = s2[::-1]
        s_l = s1[::-1]

    carry = 0
    A = [0]*10
    size = 0
    for i in range(n_s):
        sm = int(str((int(s_s[i]) + int(s_l[i]) + carry)))
        A[size] = str(sm % 10)
        carry = sm//10
        size += 1

    for i in range(n_s, n_l):
        sm = int(s_l[i]) + carry
        A[size] = str(sm % 10)
        carry = sm // 10
        size += 1

    res = A[:size]
    res = res[::-1]
    print("".join(res))



str1 = "19"
str2 = "198111"
find_sum(str1, str2)