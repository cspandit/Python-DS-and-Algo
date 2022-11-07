# 1
# 3 2
# 6 5 4
# 10 9 8 7
# Approach: As the pattern start with 1 'start' is initialized with 1 and  as the gap between start row start with 2 and
# increases by 1 (1<2>3<3>6<4>10) 'step' is initialized with 2. after each iteration start=start+step and step = step+1
# Note that extra variable temp_start is used to keep the value start intact.


def print_pat(n):
    start = 1
    step = 2
    for i in range(n):
        temp_start = start
        for j in range(i+1):
            print(temp_start, end=' ')
            temp_start -= 1
        start = start + step
        step += 1
        print('\r')


print_pat(4)