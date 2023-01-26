n = int(input())
m = 2

while 1:

    if n != 1:

        if n%m == 0:

            print(m)

            n /= m

            continue

        else:

            m += 1
            
            continue

    else: break
