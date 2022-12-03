def count_char(s):
    A = [0] * 256
    for x in s:
        A[ord(x)] += 1

    for i in range(len(A)):
        if A[i] != 0:
            print('{} : {}'.format(chr(i), A[i]))


count_char('chandra')