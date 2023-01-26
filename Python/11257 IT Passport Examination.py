s = 35 * 0.3
m = 25 * 0.3
t = 40 * 0.3

for i in range(int(input())):

    a, b, c, d = map(int, input().split())

    if (b < s) | (c < m) | (d < t) | (b+c+d < 55): print(a, b+c+d, "FAIL")
    else: print(a, b+c+d, "PASS")
