h, m = map(int, input().split())
cook = int(input())

time = m + cook
o = time//60

if time >= 60 :
    h = h + o
    m = time - 60 * o
    if h > 23 :
        h = h - 24
        print(h, m)
    elif h == 24 :
        print(0, m)
    else:
        print(h, m) # 모든 조건의 예외가 나오는 경우도 있다는 것을 생각하자.
else:
    print(h, time)
