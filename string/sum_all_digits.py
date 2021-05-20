def sum_digit(string):
    temp = '0'
    sm = 0
    for ch in string:
        if ch.isdigit():
            temp += ch
        else:
            sm = sm + int(temp)
            temp = '0'
    return sm + int(temp)  # Because when string end withs digit above else part will be skied


print(sum_digit('12abc20yz68'))
