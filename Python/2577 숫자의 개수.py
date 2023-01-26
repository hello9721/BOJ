a = int(input())
b = int(input())
c = int(input())

lst = list(str(a*b*c))
count = [0] * 10

for i in lst:
    count[int(i)] += 1

for i in range(10):
    print(count[i])
