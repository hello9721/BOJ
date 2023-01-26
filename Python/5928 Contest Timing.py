s = [11, 11, 11]
e = list(map(int, input().split()))

m = e[2] - s[2]
h = e[1] - s[1]
d = e[0] - s[0]

t = m + (h*60) + (d*24*60)

if t < 0 : print(-1)
else : print(t)
