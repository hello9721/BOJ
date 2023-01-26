l = list(input())

for j in range(97, 123):

    temp = 0
    
    for i in l:
        
        if ord(i) == j: temp += 1

    print(temp, end = " ")
    
