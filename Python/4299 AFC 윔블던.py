a, b = map(int, input().split())
n = a/2 + b/2
if (a + b < 0) or (a - b < 0) or ((a + b) % 2) : print(-1)
else: print(int(n), int(a-n))
