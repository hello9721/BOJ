w, h, n = map(int, input().split())

cw = w//n
ch = h//n

if w%n != 0: cw += 1
if h%n != 0: ch += 1

print(cw*ch)

