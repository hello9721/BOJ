school = ["TelecomParisTech", "Eurecom"]
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    if a*b > c*d: print(school[0])
    elif a*b < c*d: print(school[1])
    else: print("Tie")
