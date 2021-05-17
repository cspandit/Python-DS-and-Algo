# input = "ABC"  output = ["A_B_C", A_BC, AB_C, ABC]
# This is input-output problem and can be solved by drawing recursive tree. Check all_subsets problem for recursive tree
# So here choices are that for each character either we can include it with space or without pace.
# But for first character there is only once choice i.e without space


def solve(i_string, o_string):
    if len(i_string) == 0:
        print(o_string)
        return
    o_string_1 = o_string + "_" + i_string[0]
    o_string_2 = o_string + i_string[0]
    solve(i_string[1:], o_string_1)
    solve(i_string[1:], o_string_2)


if __name__ == "__main__":
    string = "ABC"
    # As for first character there is only choice i.e without space we modify input string and output accordingly
    output = string[0]
    string = string[1:]
    solve(string, output)
