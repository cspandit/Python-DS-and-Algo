n = 6
space_num = n-1
for i in range(1, n+1):
    for k in range(space_num, 0, -1):
        print(" ", end="")
    space_num -= 1
    for j in range(i, 0, -1):
        print("#", end="")
    print("\r")