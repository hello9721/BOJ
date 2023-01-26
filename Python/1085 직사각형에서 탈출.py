# x, y = 현재 위치
# 0, 0 = 왼쪽 아래
# w, h = 오른쪽 위

# 입력 = x y w h

x, y, w, h = map(int, input().split())
to_edge = [x, y, w-x, h-y]

print(min(to_edge))