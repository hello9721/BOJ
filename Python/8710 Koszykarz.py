n, c, h = map(int, input().split())

if (c - n)%h == 0: print((c - n)//h)
else: print((c - n)//h + 1)
