a = int(input())

cnt = 1
turn = 0

while 1:

    a = a - cnt

    if turn == 0:

        if a <= 0:
            
            print(abs(a))
            break
        
    else:

        if a < 0:

            print(0)
            break

    cnt += 1


    if turn == 0: turn = 1
    else: turn = 0
