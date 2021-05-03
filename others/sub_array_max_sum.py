def max_sub_array(A, sub_array_size):
    maxx = 0
    n = len(A)
    for i in range(n - sub_array_size +1):
        sub = []
        for j in range(i, i+sub_array_size):
            sub.append(A[j])
        print(sub)
        summ = sum(sub)
        if summ > maxx:
            maxx = summ

    return maxx

A = [2,3,5,2,9,7,1]
print(max_sub_array(A, 3))