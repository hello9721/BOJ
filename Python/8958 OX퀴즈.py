t = int(input())

for i in range(t):

    score = 0
    temp = input().split("X")

    for j in temp:

        if "O" in j: score += sum(range(1, len(j)+1))
        
    print(score)
    
