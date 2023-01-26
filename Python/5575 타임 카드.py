
for i in range(3):

    temp = list(map(int, input().split()))

    h = temp[3] - temp[0]
    m = temp[4] - temp[1]
    s = temp[5] - temp[2]

    if s < 0:

        s = 60 + s
        m = m - 1
        
    if m < 0:

        m = 60 + m
        h = h - 1

    print(h, m, s)
