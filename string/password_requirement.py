# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name
# and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the
# following criteria:
#
# Its length is at least 6.
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
# She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed,'
# ' can you find the minimum number of characters she must add to make her password strong?

def get_missing_count(s):
    d = {'digit': 0, 'lower': 0, 'upper': 0, 'special': 0}
    for x in s:
        if x.isdigit():
            d['digit'] = 1
        if x.isupper():
            d['upper'] = 1
        if x.islower():
            d['lower'] = 1
        if x in list('!@#$%^&*()-+'):
            d['special'] = 1

    man_count = 0
    for key in d.keys():
        if d[key] == 0:
            man_count += 1
    return man_count
def minimumNumber(n, password):
    if n > 6:
        man_count = get_missing_count(password)
        return man_count
    else:
        man_count = get_missing_count(password)
        req_len = n + man_count
        if req_len >= 6:
            return man_count
        else:
            return 6-n

print(minimumNumber(11, '#HackerRank'))