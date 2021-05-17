def reverse_string(string):
    i = len(string)-1
    new_str = ''
    while i >= 0:
        new_str = new_str + string[i]
        i -= 1

    return new_str


def reverse_string_sen(string):
    i = 0
    arr = string.split(" ")
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return " ".join(arr)


def reverse_string_recur(string, res):
    if len(string) == 0:
        return res
    res = res + string[-1]
    return reverse_string_recur(string[:-1], res)


s = "my name is alex"
print(reverse_string_recur(s, ""))
