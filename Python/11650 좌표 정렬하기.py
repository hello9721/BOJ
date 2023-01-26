t = int(input())

lst = [0] * t

for i in range(t):
    lst[i] = input().split()
    lst[i][0] = int(lst[i][0])
    lst[i][1] = int(lst[i][1])

lst.sort()


for i in range(t):
    print(lst[i][0], lst[i][1])
