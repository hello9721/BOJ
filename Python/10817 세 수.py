lst = list(map(int, input().split()))
a = lst.index(max(lst))
lst.pop(a)
print(max(lst))
