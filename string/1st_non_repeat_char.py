def first_char(string):
    count = [0]*256
    for c in string:
        count[ord(c)] += 1

    index = 0
    for x in string:
        if count[ord(x)] == 1:
            return string[index]
        index += 1


print(first_char('swiss'))