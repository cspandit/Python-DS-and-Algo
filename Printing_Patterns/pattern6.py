# A
# B B
# C C C
# D D D D
# E E E E E

def print_pat(n):
    val = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(val), end=' ')
        val += 1
        print('\n', end='')


print_pat(5)