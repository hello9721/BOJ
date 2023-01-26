        # 예제
        # 대상 배열
arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]


        # 최대값+1 개의 원소를 가진 count (0은 배열에 없으니 +1)
count = [0] * (max(arr) + 1)


        # count의 인덱스 == 배열의 원소
        # count의 원소 == 배열에서의 해당 인덱스의 갯수
for num in arr:
    count[num] += 1
        # [0, 1, 1, 2, 2, 1, 0, 1, 0, 1]


        # 정렬된 결과 값이 들어갈 리스트
result = []

        # 1부터 최대값+1 만큼 반복되면서
for i in range(1, len(count)):
        # 그 인덱스를 가진 count의 원소의 값만큼 반복
    for _ in range(count[i]):
        # 0은 반복이 안되고 1이상만 1부터 반복되어 추가되기때문에 정렬되어 들어간다.
        result.append(i)

print(result)
        # [1, 2, 3, 3, 4, 4, 5, 7, 9]
