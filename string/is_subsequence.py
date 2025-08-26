# problem is to check if s1 can be formed from s2 by removing all the letter in s2 which is not present is s1.

def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
            i += 1
        else:
            j += 1
    return len(s) == i

print(isSubsequence("abc", "ahbgdc"))