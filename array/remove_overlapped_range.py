L = [(4, 9), (20, 22), (1, 3), (24, 32), (23, 31), (40, 50), (12, 15), (8, 13)]
L.sort()
print(L)
new_list = []
start = L[0][0]
end = L[0][1]

for item in L[1:]:
    if end >= item[0]:
        if end < item[1]:
            end = item[1]
    else:
        new_list.append((start, end))
        start = item[0]
        end = item[1]
new_list.append((start, end))
print(new_list)
