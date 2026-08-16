import os
import json
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Zero cannot divide anything")
    else:
        return a/b

def is_palindrome(s):
    lower = s.lower()
    new_s = ''
    for c in lower:
        if 'a' <= c <= 'z':
            new_s += c
    print(new_s)
    l = 0
    h = len(new_s) - 1
    while l <= h:
        if new_s[l] != new_s[h]:
            return False
        l += 1
        h -= 1
    return True

def return_user():
    print("This is original return_user")
    return "John Don"

def read_from_home():
    f_path = os.path.expanduser('~/test.json')
    with open(f_path, 'r') as f:
        data = json.load(f)
    return data

def write_to_home():
    data = {'name': 'chandra', 'age':21}
    f_path = os.path.expanduser('~/test.json')
    print(f_path)
    with open(f_path, 'w') as f:
        json.dump(data, f)



write_to_home()
print(read_from_home())