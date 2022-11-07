# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def print_pat(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print('\n', end='')


print_pat(5)