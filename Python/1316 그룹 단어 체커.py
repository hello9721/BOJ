n = int(input())
lst = []
count = 0

# 단어를 모두 받아오기

for i in range(n):
    l = input()
    lst.append(l)

# 체커

for i in lst:
    st = list(set(i))   # 중복 없는 리스트 하나
    ls = list(i)        # 단어를 리스트로 하나
    temp = ls.copy()    # 그 복사본 하나
    
    for j in st:                        # st의 순서가 뒤죽박죽이므로
        t = ls.index(j)                 # t에 j의 인덱스를 하나 뽑아두고
        for k in range(len(ls[t: ])):   # 조건문이 제대로 작동하도록 t부터 끝까지 반복
            if j == ls[t+k]:            # ls에서 t부터 끝까지 반복하도록 t+k를 번호로 넣고
                temp.pop(temp.index(j)) # temp에서는 하나씩 제거되면서 ls와는 개수가 달라질 예정이므로
                                        # j의 인덱스를 따로 구해서 pop 적용
            else:
                break
    if len(temp) == 0:                  # 위의 반복문에서 요소가 다 제거가 된다면 그룹문자
        count += 1                      # 다 제거 되지 않는다면 그룹문자가 아니다.
        
print(count)
