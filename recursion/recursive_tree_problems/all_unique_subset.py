# Recursive tree of the this problem is will be exactly same as all_subset problem.
# To maintain uniqueness, we will not print output string instead we will store in a map


def sub_string(i_string, o_string, o_set):
    if len(i_string) == 0:
        o_set.add(o_string)
        return o_set
    o_string_1 = o_string
    o_string_2 = o_string+i_string[0]

    sub_string(i_string[1:], o_string_1, o_set)
    sub_string(i_string[1:], o_string_2, o_set)
    return o_set


print(sub_string("aac", "", set()))
