now = list(map(int, input().split()))

idle = [ 1, 1, 2, 2, 2, 8 ]

for i in range(6):
    a = idle[i] - now[i]

    print(a, end = " ")

print("")
