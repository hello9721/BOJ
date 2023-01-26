t = int(input())
lst = []

# 숫자 정렬 오름차순 ( 숫자는 1부터 1000000까지 )
# 1
# 시간 초과

for i in range(t):
    lst.append(int(input()))

for j in range(t):
    n = -1
    
    for i in lst:
        if n < 0:
            n = i
        elif n > i:
            n = i
        else:
            continue
        
    print(n)
    lst.pop(lst.index(n))


# 2
# 시간 초과

for i in range(t):
    lst.append(int(input()))

for j in range(t):
    
    n = max(lst)
        
    print(n)
    lst.pop(lst.index(n))


# 3
# 시간 초과

for i in range(t):
    lst.append(int(input()))

lst.sort()

for i in lst:
    print(i)

# 4
# 시간 초과를 막기위해 여러 수를 읽고 내보내야하는 부분에 sys 를 이용함

import sys

for i in range(t):
    lst.append(int(sys.stdin.readline()))   # input

lst.sort()

for i in lst:
    sys.stdout.write(f"{i}\n")              # print
