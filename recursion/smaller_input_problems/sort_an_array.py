def sort(A):
    if len(A) <= 0:
        return
    item = A.pop()
    sort(A)
    insert(A, item)

def insert(A, i):
    if len(A) == 0 or A[-1] < i:
        A.append(i)
        return
    x = A.pop()
    insert(A, i)
    A.append(x)


A = [1, 0, 5, 2]
sort(A)
print(A)