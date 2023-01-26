a, b, c = map(int, input().split())

d = max(a, b, c)

s = 0

if d == a: s = b*b + c*c
elif d == b: s = a*a + c*c
else: s = a*a + b*b

if a == b == c: print(2)
elif s == d*d: print(1)
else: print(0)
