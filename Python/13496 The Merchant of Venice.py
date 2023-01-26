for i in range(int(input())):

    n, s, d = map(int, input().split())
    gold = 0

    for j in range(n):

        a, b = map(int, input().split())

        day = a//s
        if a%s != 0: day += 1

        if d >= day: gold += b

    print(f'Data Set {i+1}:\n{gold}\n')
