lst = [0] * 10

for i in range(10):
    lst[i] = int(input())%42

lst = set(lst)

print(len(lst))
