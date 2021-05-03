def find_max_item(array, window_size, n):
    start = 0
    end = 0
    max_list = []
    while end < n:
        x = len(max_list)
        while x > 0:
            if max_list[x-1] < array[end]:
                max_list.pop(x-1)
                x -= 1
            else:
                break
        max_list.append(array[end])

        if end - start + 1 < window_size:
            end += 1

        elif end - start + 1 == window_size:
            print(max_list[0])
            if array[start] == max_list[0]:
                max_list.pop(0)

            start += 1
            end += 1


A = [1, 3, -1, 2, 4, 6, 5]
n = len(A)
find_max_item(A, 3, n)