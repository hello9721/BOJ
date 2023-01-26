t = int(input())

lst = list(map(int, input().split()))

check = sorted(set(lst))

dic = {check[i]:i for i in range(len(check))}
# for문을 돌려서 lst 요소 하나하나의 인덱스를 찾는다면 = O(n)

for i in range(t):
    print(dic[lst[i]], end = " ")
