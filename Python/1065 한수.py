t = int(input()) + 1

lst = [0] * (t)

for i in range(1, t):
    if i < 100:
        lst[i] = 1
    else:
        a = list(str(i))
        x = int(a[0]) - int(a[1])
        y = int(a[1]) - int(a[2])
        if i < 1000:
            if x == y:
                lst[i] = 1

print(lst.count(1))
