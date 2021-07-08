# An anagram of a string is another string that contains the same characters,
# only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.


from collections import defaultdict

# by sorting
def check_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# using map
def check_anagram_map(s1, s2):
    if len(s1) != len(s2):
        return False

    d = defaultdict(int)
    count = 0
    for c in s1:
        d[c] += 1
        if d[c] == 1:
            count += 1

    for cc in s2:
        d[cc] -= 1
        if d[cc] == 0:
            count -= 1
    if count == 0:
        return True
    else:
        return False


print(check_anagram_map("spot", "pots"))