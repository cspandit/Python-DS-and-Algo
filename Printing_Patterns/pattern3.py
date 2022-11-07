#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# number space required is k = n-1

def print_pat(n):
    k = n-1
    for i in range(n):
        for j in range(k):
            print(end=' ')
        k = k-1
        for j in range(i+1):
            print("*", end=' ')
        print('\n', end='')

print_pat(5)