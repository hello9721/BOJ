lst = list(map(int, input().split()))
a = 0

for i in lst:
    a += i*i

print(a%10)
