def decimal_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = len(num)-1

    roman = ""
    while number:
        base = number//num[i]
        number = number % num[i]
        roman = roman + sym[i]*base
        i = i-1
    return roman


print(decimal_to_roman(1000))