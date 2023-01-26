a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

t = 0

if a < 0: t = abs(a)*c + d + b*e
else: t = (b - a) * e

print(t)
