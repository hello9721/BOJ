import sys

n = int(input())

lst = [0] * n

for i in range(n):
    lst[i] = int(sys.stdin.readline())


    # 산술 평균

if round(sum(lst)/n, 0) == -0.0:    # -0.n 일 경우 반올림 하면 -0이 된다.
    print("0")                      # 이경우를 막기 위한 조건문
else:
    print(f"{sum(lst)/n:.0f}")


    # 중앙값

lst.sort()

print(lst[int(n/2)])


    # 최빈값
    # 여러개일 경우 두번째로 작은 값

counts = [1]
count = 1

if n == 1:                          # 갯수가 하나 일 경우 그대로 출력
    print(lst[0])
else:
    for i in range(1,n):            # 정렬된 배열과 그와 대응하는 카운팅 배열을 만들기
        if lst[i] == lst[i-1]:
            count += 1
            counts.append(count)
        else:
            count = 1
            counts.append(count)
            
    a = counts.count(max(counts))
    m = counts.index(max(counts))
    
    if a > 1:                       # 최빈값이 여러개일 경우
        counts.pop(m)               # 제일 작은 최빈값을 없앤 후
        m = counts.index(max(counts)) + 1
        
    print(lst[m])                   # 최빈값 출력


    # 범위
    
print(lst[-1]-lst[0])               # 정렬된 배열의 마지막 원소와 첫 원소의 뺄셈
