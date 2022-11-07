# *
# * *
# * * *
# * * * *
# * * * * *

def print_pat(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print('\n', end='')

def print_pat_recur(n):
    if n == 0:
        return
    print_pat(n-1)
    print('* '*n)

print_pat_recur(5)