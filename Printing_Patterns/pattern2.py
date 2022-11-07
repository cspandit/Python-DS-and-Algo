#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# Formula to calculate empty_space(k) = n*2-2

def print_pat(n):
    k = 2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k = k-2
        for j in range(i+1):
            print('*', end=' ')
        print('\n', end='')

print_pat(5)