# Given a string consisting of opening and closing parenthesis,
# find the length of the longest valid parenthesis substring.

# Examples:
#
# Input : ((()
#           Output : 2
#           Explanation : ()
#
#     Input: )()())
# Output : 4
# Explanation: ()()
#
# Input:  ()(()))))
# Output: 6
# Explanation:  ()(())


def longest_substring(string):
    stack = [-1]
    res = 0
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            if len(stack) > 0:
                res = max(res, (i - stack[-1]))
            else:
                stack.append(i)
    return res


s = "()(()))))"
print(longest_substring(s))
