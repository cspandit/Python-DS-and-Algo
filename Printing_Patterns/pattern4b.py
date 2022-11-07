# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

def print_pat(n):
    for i in range(n):
        for j in range(n-i):
            print(i+1, end=' ')
        print('\r')


print_pat(5)