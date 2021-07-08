import math

def print_z(n):
    while n % math.sqrt(n) != 0:
        n += 1
    print(n)
    m = int(math.sqrt(n))
    print(m)
    count = 1
    for i in range(m):
        for j in range(m):
            if i != 0 and i != m-1:
                if i == m-j-1:
                    print(" {}".format(count), end=" ")
                    count += 1
                else:
                    print(" ", end=" ")
            else:
                print("{} ".format(count), end=" ")
                count += 1

        print("\r")
print_z(10)
