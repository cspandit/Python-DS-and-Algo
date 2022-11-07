# LeetCode-119
# Pascal triangle is used to calculate Binomial expansion: nCr = n!/r!*(n-r) ! Lets say nCr is represented by (n,r)

#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#  1 5 10 10 5 1
# 1 6 15 20 15 6 1

            #             (0,0)
            #         (1,0)   (1,1)
            #     (2,0)   (2,1)   (2,2)
            # (3,0)   (3,1)   (3,2)   (3,3)

# If you do calculation in 2nd pattern using above formula, it will give 1st patter. So both the pattern are same
# the approach is to use previous value in each row to calculate the current value of the row. Say if we want to
# calculate nCr then we can use value of nCr-1 and the relation is nCr = nCr/nCr-1. After simplification
# nCr/nCr-1 =(n-r+1)/r, which gives nCr = nCr-1*((n-r+1)/r)

def pascal_triangle(n):
    space = n-1
    for rowIndex in range(n):
        row = [1]
        for j in range(1, rowIndex+1):
            row.append(row[j-1]*(rowIndex-j+1)//j)  # rowIndex represent 'n' and 'j' represent 'r' in formula
        print(" "*space, end='')
        space = space-1
        print(" ".join([str(i) for i in row]))


pascal_triangle(6)