    # 성공한 정답

import sys

t = int(input())

age = [0] * t

for i in range(t):
    temp = sys.stdin.readline().split()
    
    age[i] = [str(temp[0]), str(temp[1])]

age.sort(key = lambda a: int(a[0]))

                        # sort의 key 속성은 함수가 그 값으로 와야하는데
                        # 단일인자를 매개변수로 주고 나오는 반환값을 기준으로 정렬

                        # lambda 함수 => lambda x: x[0]
                        # def temp(x):
                        #    return x[0]
                        # x를 매개변수로 받아 x[0]을 반환

for i in range(t):
    sys.stdout.write(f"{age[i][0]} {age[i][1]}\n")


    # 실패 1
    # 시간초과

import sys

t = int(input())

age = [0] * t
name = [0] * t

for i in range(t):
    temp = sys.stdin.readline().split()
    
    age[i] = [int(temp[0]), i]
    name[i] = [i, temp[1]]

age.sort()

for i in range(t):
    for j in range(t):
        if age[i][1] == name[j][0]:
            age[i][1] = name[j][1]
        else:
            continue
    sys.stdout.write(f"{age[i][0]} {age[i][1]}\n")

    # 실패 2
    # 시간초과

import sys

t = int(input())

age = [0] * 201
name = [0] * t

for i in range(t):
    temp = sys.stdin.readline().split()
    
    age[int(temp[0])] += 1
    name[i] = [temp[0], temp[1]]

for i in range(1, 201):
    if age[i] > 0:
        x = age[i]
        n = 0
        while x > 0:
            if name[n][0] == i:
                sys.stdout.write(f"{i} {name[n][1]}")
                name[n][0] -= 201
                x -= 1
            else:
                n += 1
