"""
To find the length of the longest palindrome that can be built from a given string s (case-sensitive), you can follow this logic:

Key Observations:
A palindrome has pairs of characters mirrored around the center.
Characters that appear an even number of times can be fully used.
Characters that appear an odd number of times can contribute all but one of their occurrences(n-1)
At most one character with an odd count can be placed in the center of the palindrome.

Example
Input: s = "aaabccccdd"
Output: 9
Explanation: One longest palindrome that can be built is "adccaccda"/"adccbccda", whose length is 9.
"""


def longestPalindrome(s):
    d = dict.fromkeys(s, 0)
    for x in s:
        d[x] += 1
    pali_length = 0
    found_odd = False
    for i in d.values():
        if i % 2 == 0:
            pali_length += i
        else:
            pali_length += (i - 1)
            found_odd = True
    if found_odd:
        pali_length += 1
    return pali_length

print(longestPalindrome("aaabccccdd"))
