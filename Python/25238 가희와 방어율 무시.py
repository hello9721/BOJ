a, b = map(int, input().split())

c = a/100 * b

if a - c >= 100: print(0)
else: print(1)
