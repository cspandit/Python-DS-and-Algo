# SYMBOL       VALUE
# I            1
# IV           4
# V            5
# IX           9
# X            10
# XL           40
# L            50
# XC           90
# C            100
# CD           400
# D            500
# CM           900
# M            1000
# Approach: A number in Roman Numerals is a string of these symbols written in descending order
# (e.g. M’s first, followed by D’s, etc.). However, in a few specific cases, to avoid four characters being repeated
# in succession(such as IIII or XXXX), subtractive notation is often used as follows:
#
# I placed before V or X indicates one less, so four is IV (one less than 5) and 9 is IX (one less than 10).
# X placed before L or C indicates ten less, so forty is XL (10 less than 50) and 90 is XC (ten less than a hundred).
# C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and
# nine hundred is CM (a hundred less than a thousand).

def roman_to_decimal(string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    res = 0
    while i < len(string):
        s1 = d[string[i]]
        if i+1 < len(string):
            s2 = d[string[i+1]]
            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2-s1
                i = i+2
        else:
            res = res + s1
            i = i + 1
    return res


print(roman_to_decimal('MCMIV'))