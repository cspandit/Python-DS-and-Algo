# This problem is very similar to permutation_with_case problem where input was always lower case string
# But in this case input string can contain both upper and lower case letter as well as integer.
# input : "a1B2" [a1B2, A1b2, a1b1, A1B1]
# While drawing recursive tree for this problem, for all char we have to choices, either upper or lower.
# But for a integer we have only one choice, we just include it in output


def solve(i_string, o_string):
    if len(i_string) == 0:
        print(o_string)
        return

    if i_string[0].isdigit():
        o_string = o_string + i_string[0]
        solve(i_string[1:], o_string)
    else:
        o_string_1 = o_string + i_string[0]
        if i_string[0].islower():
            o_string_2 = o_string + i_string[0].upper()
        else:
            o_string_2 = o_string + i_string[0].lower()
        solve(i_string[1:], o_string_1)
        solve(i_string[1:], o_string_2)


solve("a1B2", "")
