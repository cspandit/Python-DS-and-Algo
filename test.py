from collections import defaultdict
def check_palindrome(s):
    d = defaultdict(int)
    for x in s:
        d[x] += 1

    odd_count = 0
    for x in s:
        if d[x]%2 != 0:
            odd_count += 1
    if odd_count > 1:
        return False
    else:
        return True

s = 'aabbcd'
print(check_palindrome(s))

