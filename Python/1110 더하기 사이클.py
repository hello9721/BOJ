n = input()

count = 0

a = '0'
b = '0'

if int(n) < 10:
    
    b = n
    
else:
    
    a = n[0]
    b = n[1]

while 1:

    temp = int(a) + int(b)
            
    if (count > 0) & (int(a+b) == int(n)):
                                    # & 또한 연산자 이기에 우선순위를 고려해야함.        
        print(count)
        
        break
        
    else:

        count += 1

        a = b[0]
        
        if temp < 10: b = str(temp)
        else: b = str(temp)[1]
        
        continue
        
