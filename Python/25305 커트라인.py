n, k = map(int, input().split())

lst = input().split()

for i in range(len(lst)):
    lst[i] = int(lst[i])

lst.sort(reverse = True)

print(lst[k-1])

