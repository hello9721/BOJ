c = int(input())

for i in range(c):

    temp = input().split(" ", 1)
    count = 0

    num = int(temp[0])
    score = list(map(int, temp[1].split()))
    mean = sum(score)/num

    for j in score:

        if j > mean: count += 1

    print(f"{count/num * 100:.3f}%")
