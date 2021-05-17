# This problem can be approached by designing recurssive tree

#                                        op:"":ip:"ab"
#                                          /         \
#                                         /           \
#                                        /             \
#                              op:"";ip:"b"                op:"a";ip:"b"
#                                      / \                    /     \
#                                     /   \                  /       \
#                                    /     \                /         \
#                             op:"";ip:""  op"b";ip:""   op:"a";ip:""   op:"ab"; ip:""

# At each step one time 1st item in ip string is included in op other time not
# output is when when put becomes empty.
# Difference b/w subset, substring and sub subsequence
# Lets say given string is "abc"
# subset = ["", a, b, c, ab, bc, ac, abc]
# substring = Sub string are always continuous. ac is not continuous in abc
# subsequence = here order of a character in a give string matters. It should be maintained while making subsequence
#               for "abc", ac is subsequence but ca is not

# All substrings are subsequences and all subsequences are subset


def sub_string(i_string, o_string):
    if len(i_string) == 0:
        if len(o_string) == 0:
            print("''")
        else:
            print(o_string)
        return
    o_string_1 = o_string
    o_string_2 = o_string+i_string[0]

    sub_string(i_string[1:], o_string_1)
    sub_string(i_string[1:], o_string_2)


sub_string("abc", "")
