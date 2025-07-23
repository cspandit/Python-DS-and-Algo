x = 12345
def reverse(n):
    r_num = 0
    while n:
        v = n%10
        r_num  = r_num*10+v
        n = n//10
    return r_num

print(reverse(x))
