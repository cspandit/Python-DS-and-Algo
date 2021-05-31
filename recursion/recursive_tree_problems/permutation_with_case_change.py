# permutation word in problem is misleading. As we are not actually calculating permutation.
# This is just subset problem where we have two choices : upper and lower
# input = "ab"  output = ["AB", Ab, aB, ab]
# This is input-output problem and can be solved by drawing recursive tree. Check all_subsets problem for recursive tree
# So here choices are that each character either can be upper case or lower case


def solve(i_string, o_string):
    if len(i_string) == 0:
        print(o_string)
        return

    o_string_1 = o_string + i_string[0]
    o_string_2 = o_string + i_string[0].upper()
    solve(i_string[1:], o_string_1)
    solve(i_string[1:], o_string_2)


solve("abc", "")