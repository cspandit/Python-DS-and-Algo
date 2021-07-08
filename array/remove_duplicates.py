# iterative approach O(nlogn)

a = [1, 2, 9, 7, 5, 1, 2, 3]
a.sort()
print(a)
item = a[-1]
for i in range(len(a)-2, -1, -1):
    if a[i] == item:
        del(a[i])
    else:
        item = a[i]

print(a)