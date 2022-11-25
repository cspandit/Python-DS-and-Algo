def digitSum(s, k):
    res = s
    while len(res) > k:
        n = len(res)
        tem_res = ''
        j = 0
        while j < n:
            if j+k <= n:
                k_s = res[j:j+k]
                sm = 0
                for x in k_s:
                    sm = sm + int(x)
                tem_res += str(sm)
                j += k
            else:
                break
        sm = 0
        if j < n:
            while j < n:
                sm += int(res[j])
                j += 1
            tem_res += str(sm)
        res = tem_res

    return res


print(digitSum("00000000", 3))
