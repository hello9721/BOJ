# height = 4*n / width = 7
# hours = [4, 6, 4, 10]

w = int(input())

mor = ['0']
aft = ['0']
eve = ['0']
mid = ['0']

for i in range(w):

    for j in range(4):

        if j == 0: mor += list(input().split())
        elif j == 1: aft += list(input().split())
        elif j == 2: eve += list(input().split())
        else: mid += list(input().split())

check = list(set(mor+aft+eve+mid))
check.sort()

if '-' in check: check = check[2: ]
else: check = check[1: ]

t = [0] * len(check)

for i in check:

    if i in mor: t[check.index(i)] += mor.count(i) * 4
    if i in aft: t[check.index(i)] += aft.count(i) * 6
    if i in eve: t[check.index(i)] += eve.count(i) * 4
    if i in mid: t[check.index(i)] += mid.count(i) * 10

if check == []: print("Yes")
elif max(t)-min(t) <= 12: print("Yes")
else: print("No")
