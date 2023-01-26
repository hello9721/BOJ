n = 10001

lst = [0] * n

for i in range(1, n):
    if i < 10:
        a = i + i + 0
    else:
        b = list(str(i))
        a = i
        for j in range(len(b)):
            a = a + int(b[j])
    if a < n:
        lst[a] = 1
    a = 0               # i 일때 범위를 넘어가더라도 i+1 일때는 범위 내 일수도 있음

for i in range(1, len(lst)):
    if lst[i] == 0:
        print(i)
