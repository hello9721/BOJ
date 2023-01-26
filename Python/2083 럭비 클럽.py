while 1:

    t = input()

    if t == "# 0 0": break

    n = t.split()[0]
    a = t.split()[1]
    w = t.split()[2]

    if ( int(a) > 17 ) | ( int(w) >= 80 ): print(n, "Senior")
    else: print(n, "Junior")
