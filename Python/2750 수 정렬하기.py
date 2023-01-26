t = int(input())
lst = []

# 숫자 정렬 오름차순 ( 숫자는 1부터 1000까지 )

for i in range(t):
    lst.append(int(input()))

n = 1001

for j in range(t):
    for i in lst:
        if n > i:
            n = i
        else:
            continue
    print(n)
    lst.pop(lst.index(n))
    n = 1001
