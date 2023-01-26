n, m, k = map(int, input().split())

if k >= m:
    x = k%m
    y = k//m
else:
    x = k
    y = 0


print(y, x)
