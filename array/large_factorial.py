def factorial(n):
    res = [None]*500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x+1

    return res[:res_size]


def multiply(x, res, res_size):
    carry = 0
    i = 0
    while i < res_size:
        prod = res[i]*x + carry
        res[i] = prod % 10
        carry = prod // 10
        i += 1

    while carry:
        res[i] = carry
        carry = carry//10
        res_size += 1

    return res_size


result = factorial(5)
for i in range(len(result)-1, -1, -1):
    print(result[i], end="")
