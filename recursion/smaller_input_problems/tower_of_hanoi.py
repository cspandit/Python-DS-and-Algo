def t_o_h(n, s=1, h=2, d=3):
    if n == 1:
        print("Move from %s to %s" % (s, d))
        return
    t_o_h(n-1, s, d, h)
    print("Move from %s to %s" % (s, d))
    t_o_h(n-1, h, s, d)


t_o_h(2)
