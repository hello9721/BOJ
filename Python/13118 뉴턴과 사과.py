p = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x not in p: print(0)

for i in range(4):

    if x == p[i]: print(i+1)
