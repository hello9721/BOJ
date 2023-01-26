# 메모리 초과

import sys

t = int(input())
lst = []

for i in range(t):
    lst.append(int(sys.stdin.readline()))   # input

lst.sort()

for i in lst:
    sys.stdout.write(f"{i}\n")              # print

# 계수 정렬 ( Counting Sort ) 사용
# 1부터 10000까지의 자연수가 최대 10000000개 주어짐.
# 중복되는 경우가 많을 것으로 예상되기 때문에 메모리 낭비를 줄이기 위해 사용.

t = int(input())

count = [0] * 10001

# for 안에서 append는 비효율적이 될수도 있기에 미리 공간마련.
# 원소의 최대값 + 1 개

for i in range(t):
    a = int(sys.stdin.readline())
    count[a] += 1

for i in range(1, len(count)):
    for j in range(count[i]):
        print(i)
