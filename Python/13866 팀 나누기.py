from itertools import product as p          # 2개 이상의 리스트를 조합하여 반환

l = list(map(int, input().split()))
t = []

for i in p(l[ :2], l[2: ], repeat = 1): t.append(sum(i))

print( min(abs(t[0]-t[3]), abs(t[1]-t[2])) )
                                            # 0번째와 3번째, 1번째와 2번째가 요소의 중복 없음 
                                            # 뒤의 요소가 더 크면 -가 나오기에 절대값으로 처
