s1 = "0100,0011,1010,1001"
s2 = s1.split(',')
num = []
for s in s2:
    n = 0
    for i, v in enumerate(s[::-1]):
        n += 2**int(i)*int(v)
    num.append(n)
print(num)