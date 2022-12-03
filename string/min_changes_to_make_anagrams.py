# minimum number to make two string anagrams

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
    print(count//2)

def make_anagrams_array(s1, s2):
    A = [0]*26
    count = 0
    for x in s1:
        A[ord(x)-ord('a')] += 1

    for x in s2:
        A[ord(x)-ord('a')] -= 1

    for x in A:
        count += abs(x)

    print(count//2)


s1 = "ddcf"
s2 = "cedk"
make_anagrams_array(s1, s2)