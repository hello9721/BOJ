t = int(input())

for i in range(t):

    temp = input().split()

    r = int(temp[0])
    word = list(temp[1])

    for i in word:
        print(i * r, end = "")
    print("")
