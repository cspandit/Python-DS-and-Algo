# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


def palindrome(string):
    string = string.lower()
    print(string)
    new_string = ''

    for c in string:
        if ('a' <= c <= 'z') or ('0' <= c <= '9'):
            new_string = new_string + c

    rev_string = ''
    j = len(new_string)-1
    while j >= 0:
        rev_string = rev_string + new_string[j]
        j -= 1

    print(new_string)
    print(rev_string)
    return new_string == rev_string


print(palindrome("A man, a plan, a canal: Panama"))
