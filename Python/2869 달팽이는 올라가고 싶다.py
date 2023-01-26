# 1
# 시간초과

a, b, v = map(int, input().split())

c = a - b
count = 0

while 1:
    if v > a :
        v -= c
        count += 1
    elif a >= v > 0:
        v -= a
        count += 1
    else:
        print(count)
        break


# 2

a, b, v = map(int, input().split())

c = a - b

if ( v - b ) % c == 0 :
    print(( v - b ) // c)
else:
    print(( v - b ) // c + 1)
