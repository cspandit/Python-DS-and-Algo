def reverse(num):
    while num:
        rem = num%10
        print(num%10, end="")
        num = num//10

reverse(10011)