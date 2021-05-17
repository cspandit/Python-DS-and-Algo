# Suppose on the first row, we have a 0. Now in every subsequent row, we look at the previous row and
# replace each occurrence of 0 by 0 1, and each occurrence of 1 by 1 0. Suppose we have N rows and index K,
# we have to find the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed). So if N = 4 and K = 5,
# then the output will be 1. This is because −
#        k=1   k=2     k=3     k=4    k=5     k=6      k=7    k=8
# Row 1: 0
# Row 2: 0      1
# Row 3: 0      1       1       0
# Row 4: 0      1       1       0       1       0       0       1

# This problem is completely based on observations :
# 1. length if Nth row is 2**(N-1).
# 2. for any Nth row, value of K from 1 to mid of the row is exactly same as value of K in previous row
# 3. for for any Nth row, value of K from mid of the row to end of the row is complement of value of K in prev row

# For any row N>1 we know that there exist previous row, so in process of making problem small we can do N = N-1
# But for any column K we cannot say there exist a value for K-1 in prev row. We use above abservation to decrease K


def kth_grammer(N, K):
    if N == 1 and K == 1:
        return 0       # Base condition is given in problem
    mid = 2**(N-1)//2  # 2**(N-1) is length of Nth row
    if K <= mid:
        return kth_grammer(N-1, K)
    else:
        return not kth_grammer(N-1, K-mid)


print(kth_grammer(4, 4))
