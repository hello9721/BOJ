lst = ['a','b','c','d']
p = [1,2,3,4]
m = int(input())

case1 = []
case2 = []

for i in range(4):
    
    for j in range(i+1, 4):
        
        if sum(p[i:j+1]) < m:

            s = []
            
            for k in range(len(p[i:j])):
                
                s.append(lst[i:j][k])
                
            s.append(lst[j])
            s.append(sum(p[i:j+1]))

            case1.append(s)

for i in range(4):
    
    temp = lst.copy()
    price = p.copy()
    temp.pop(lst.index(lst[i]))
    price.pop(p.index(p[i]))

    print(temp, price)

    cnt = 0
    
    for j in range(cnt+1, 3):
        
        if sum(price[cnt:j+1]) < m:

            s = []
            for k in range(len(price[cnt:j])):
                
                s.append(temp[cnt:j][k])
                
            s.append(temp[j])
            s.append(sum(price[cnt:j+1]))

            print(s)

            case2.append(s)
            
            cnt += 1
