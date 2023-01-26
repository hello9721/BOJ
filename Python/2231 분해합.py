# N = abc + a + b + c
# abc는 N의 생성자
# 1 <= N <= 1000000

# 입력 = N
# 출력 = 가장 작은 생성자

## 방법 1 -> 30616 KB / 1740 ms

n = int(input())
op = 0

for i in range(1, n + 1):

    cnt = i
    temp = str(i)
    for j in temp: i += int(j)

    if n == i:
        
        op = cnt
        break

print(op)

## 방법 2 -> 30616 KB / 1180 ms

n = int(input())
op = 0

for i in range(1, n + 1):

    plus = sum(map(int, str(i)))
    plus += i

    if n == plus:
        
        op = i
        break

print(op)