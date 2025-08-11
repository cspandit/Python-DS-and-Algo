"""
n=6
1 2 3 4 5 6
        7
      8
    9
  0
1 2 3 4 5 6
"""


def print_z(n):
    count = 1
    for i in range(n):
        count = count % 10
        for j in range(n):
            if i == 0 or i == n - 1:
                print(count, end=" ")
                count += 1
            elif j == n - i - 1:
                print(count, end=" ")
                count += 1
            else:
                print(" ", end=" ")
        print('\r')



print_z(6)
