# Here at start we have n choices, n being the length of input string
# choices are swapping 1st char with element from 1st to last.
# In second recursive call we fix 1st char and do the same process from 2nd to last


def permute(string, l, h):
    if l == h:
        print(''.join(string))
        return
    else:
        for i in range(l, h):
            string[l], string[i] = string[i], string[l]
            permute(string, l+1, h)
            string[l], string[i] = string[i], string[l]  # so that for other choices string remain unchanged


s = "ABC"
permute(list(s), 0, len(s))
