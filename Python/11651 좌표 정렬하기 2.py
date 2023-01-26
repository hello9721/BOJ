t = int(input())

yx = [0] * t


for i in range(t):
    temp = input().split()

    yx[i] = [int(temp[1]), int(temp[0])]

yx.sort()

for i in range(t):
    print(yx[i][1], yx[i][0])
