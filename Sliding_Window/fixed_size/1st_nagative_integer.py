def first_negative(array, window_size, n):
    start = 0
    end = 0
    list_negative = []
    while end < n:
        if array[end] < 0:
            list_negative.append(array[end])
        if end - start + 1 < window_size:
            end += 1
        elif end - start + 1 == window_size:
            if len(list_negative) == 0:
                print(0, end=" ")
            else:
                print(list_negative[0])
                if array[start] == list_negative[0]:
                    list_negative.pop(0)
            start += 1
            end += 1


A = [12, -1, -7, 8, 10, -6, 7, 10, 12]
n = len(A)
first_negative(A, 3, n)