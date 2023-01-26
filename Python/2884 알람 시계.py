h, m = map(int, input().split())

m = m - 45

if m >= 0: print(h, m)
else:
    m = 60 + m
    h = h - 1

    if h >= 0: print(h, m)
    else: print(24 + h, m)
