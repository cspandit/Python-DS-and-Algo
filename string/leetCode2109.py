# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original
# string where spaces will be added. Each space should be inserted before the character at the given index.
#
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices
# 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".

def addSpaces(s, spaces):
    res = ''

    def space(temp_res, s, start_i, end_i):
        while start_i < end_i:
            temp_res += s[start_i]
            start_i += 1
        temp_res += ' '
        return temp_res

    res = space('', s, 0, spaces[0])
    i = 1
    while i < len(spaces):
        res = space(res, s, spaces[i - 1], spaces[i])
        i += 1
    res += s[spaces[-1]:]
    return res

print(addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))