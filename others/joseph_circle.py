def get_alive(n, k):
    A = []
    for i in range(n):
        A.append(1)
    print(A)

    sword = 0
    dead = 0
    shift = 1
    while dead < n-1:
        while shift <= k:
            shift += 1
            shift = shift % n
            if A[shift] == 1:
                shift +=1


get_alive(7, 3)