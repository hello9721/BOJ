burger = [0] * 3
T = [0] * 2

set = [0] * 6

a = 0

burger[0] = int(input())
burger[1] = int(input())
burger[2] = int(input())
T[0] = int(input())
T[1] = int(input())

for i in burger:
    
    for j in T:
        
        set[a] = i + j - 50
        a += 1

print(min(set))
