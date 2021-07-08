# Problem is if given two strings s1 and s2, check if s2 is rotation of s1.
# Example : s1 = ABCD and s2 CDAB => True
#           s1 = ABCD and s2 ACBD => False

# Solution: concatenate s1 with itself(s1+s1 = ABCDABCD) and check if s2 is sub string of new result string
# checking substring can be asked to do in O(n)

# Complexity O(n^2)
def is_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    for i in range(m-n+1):
        sub_string = ""
        for j in range(i, i+n):
            sub_string = sub_string + s1[j]
        if sub_string == s2:
            return True
    return False

# Complexity O(n)
def is_substring_sliding_window(s1, s2):
    i = 0; j = 0
    k = len(s2)
    n = len(s1)
    sub_string = []
    while j < n:
        sub_string.append(s1[j])
        if len(sub_string) < k:
            j += 1
        elif len(sub_string) == k:
            if "".join(sub_string) == s2:
                return True
            sub_string = sub_string[1:]
            i += 1
            j += 1
    return False

def is_rotation(s1, s2):
    s1 = s1+s1
    print(is_substring_sliding_window(s1, s2))


is_rotation("ABCD", "CDAB")
