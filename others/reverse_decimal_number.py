def reverse(num):
    while num:
        rem = num%10
        if rem == 0 and num/10 != 0:
            print(0, end='')
        else:
            print(num%10, end="")
        num = num//10

reverse(10011)