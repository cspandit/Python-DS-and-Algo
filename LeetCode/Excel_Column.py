"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
"""


def convertToTitle(columnNumber):
    res = ""
    while columnNumber > 0:
        rem = columnNumber % 26
        if rem == 0:
            res = res + 'Z'
            columnNumber = columnNumber // 26 - 1
        else:
            res = res + chr((rem - 1) + ord('A'))
            columnNumber = columnNumber // 26
    return res[::-1]


print(convertToTitle(53))
