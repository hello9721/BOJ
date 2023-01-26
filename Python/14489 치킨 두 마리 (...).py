a, b = map(int, input().split())
c = int(input())

d = a + b

if d - c*2 >= 0: d = d - c*2

print(d)
