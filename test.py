# This is to run quick code
x = 12345
def reverse(num):
    count = 0
    while num:
        i = num%10
        num = num//10
        count += 1
    return count
print(reverse(x))
