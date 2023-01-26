l = [0] * 6

for i in range(6): l[i] = int(input())

a = min(l[0:4])
b = min(l[4:6])

print(sum(l)-a-b)
