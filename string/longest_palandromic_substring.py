# Condition of string itself being a palindrome should be ignored.
# Extra space can be improved by including code to check palindrome inside 2nd for loop. Time complexity will be O(N^3)

def longest_palindrome(string):
    sub_list = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub_list.append(string[i:j])
    # print(sub_list)

    max_sub = ""
    for sub in sub_list:
        if sub == string:
            continue
        l = 0
        h = len(sub)-1
        is_palindrome = True
        while l < h:
            if sub[l] != sub[h]:
                is_palindrome = False
                break
            l += 1
            h -= 1
        if is_palindrome:
            if len(max_sub) < len(sub):
                max_sub = sub
    return max_sub


print(longest_palindrome("forgeeksskeegfor"))