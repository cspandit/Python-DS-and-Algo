"""
You are given two strings s and t. In one step, you can append any character to either s or t.
Return the minimum number of steps to make s and t anagrams of each other.
An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example :
Input: s = "leetcode", t = "coats"
Output: 7
Explanation:
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
"""

def make_anagrams(s1, s2):
    d1 = dict.fromkeys(s1, 0)
    count = 0
    for x in s1:
        d1[x] += 1

    for y in s2:
        if y in d1:
            d1[y] -= 1
        else:
            d1[y] = 1

    print(d1)
    for x in d1.keys():
        count += abs(d1[x])
    print(count)

def make_anagrams_array(s1, s2):
    A = [0]*26
    count = 0
    for x in s1:
        A[ord(x)-ord('a')] += 1

    for x in s2:
        A[ord(x)-ord('a')] -= 1

    for x in A:
        count += abs(x)

    print(count)


s1 = "leetcode"
s2 = "coats"
make_anagrams(s1, s2)