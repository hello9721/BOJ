n, m = map(int, input().split())

lst = [0] * 2*n

for i in range(2*n):
    lst[i] = input()

for i in range(n):
    for j in range(m):
        a = lst[i].split()[j]
        b = lst[i+n].split()[j]

        print(int(a)+int(b), end = ' ')
    print('')
