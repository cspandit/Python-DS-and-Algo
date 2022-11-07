# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

n = 5
count = 5
for i in range(n):
    for j in range(i+1, 0, -1):
        print(j, end=' ')
    print('\r')