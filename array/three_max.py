def three_max(array):
    f_max = -1
    s_max = -1
    t_max = -1
    for i in range(len(array)):
        if array[i] > f_max:
            t_max = s_max
            s_max = f_max
            f_max = array[i]

        elif array[i] > s_max:
            t_max = s_max
            s_max = array[i]

        elif array[i] > t_max:
            t_max = array[i]

    return f_max, s_max, t_max


A = [12, 13, 1, 10, 34, 1]
print(three_max(A))