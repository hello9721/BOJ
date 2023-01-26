l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

day1 = 0
day2 = 0

if a%c == 0: day1 = a//c
else: day1 = a//c + 1

if b%d == 0: day2 = b//d
else: day2 = b//d + 1

print(l-max(day1, day2))
