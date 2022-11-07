# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def print_pat(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print('\r')


print_pat(5)