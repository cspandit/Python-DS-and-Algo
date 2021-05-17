def sort(array):             # Array is [1, 0, 5, 2]
    if len(array) == 1:      # Lets say when size of an array is 1 it is sorted
        return
    item = array.pop()       # item is last element : 2
    sort(array)              # Hypothesis is sort([1, 0, 5,]) will give : [0, 1, 5]
    insert(array, item)      # Now all we have to do is insert item at correct pos in [0, 1, 5]


def insert(array, item):                    # Array : [0, 1, 5], item = 2
    if len(array) == 0 or array[-1] < item:
        array.append(item)
        return
    temp = array.pop()                      # temp = 5
    insert(array, item)                     # Hypothesis is insert([0, 1], item) will give : [0, 1 ,2]
    array.append(temp)                      # Now just add temp = 5 at the end : [0, 1, 2, 5]


A = [1, 0, 5, 2]
sort(A)
print(A)
