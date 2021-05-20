# Given two strings string1 and string2, the task is to find the smallest substring in string1 containing all
# characters of string2 efficiently.
# Input: string = “this is a test string”, pattern = “tist”
# Output: Minimum window is “t stri”
# Explanation: “t stri” contains all the characters of pattern.

# Solution 1 : a. final all the sub string

#              b. find all the substring containing all the chars of string 2
#              c. Find min length substring containing all the chars of string 2

from collections import defaultdict

def sub_string(s):
    sub_list = []
    n = len(s)
    for i in range(n):
        sub = ""
        for j in range(i+1, n+1):
            sub_list.append(s[i:j])
    return sub_list

def min_lenght_sub_string(s1, s2):
    sub_list = sub_string(s1)
    min_sub = s1
    for sub in sub_list:
        if len(sub) < len(s2):
            continue
        d = defaultdict(int)
        for ch in s2:
            d[ch] += 1

        count = len(d)
        j = 0
        while count > 0 and j < len(sub):
            if sub[j] in d:
                d[sub[j]] -= 1
                if d[sub[j]] == 0:
                    count -= 1
            j += 1
        if count == 0:
            if len(min_sub) > len(sub):
                min_sub = sub
    return min_sub


# Solution 2 : Sliding window problem Check min_window_substring problem
print(min_lenght_sub_string("geeksorfgeeks", 'ksf'))

