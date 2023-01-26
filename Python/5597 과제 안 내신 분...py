lst = [0] * 31

for i in range(28):

    a = int(input())

    lst[a] = 1

lst[0] = 1
n = lst.index(0)

print(n)

lst[n] = 1
n = lst.index(0)

print(n)
