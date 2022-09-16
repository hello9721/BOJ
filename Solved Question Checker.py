b = """
Sprout 1000
A+B
 
STANDARD
199,795
2.40
Sprout 1001
A-B
 
STANDARD
168,665
1.41
Sprout 1008
A/B
 
STANDARD
131,996
2.86
Bronze V 1271
엄청난 부자2
"""

# 위의 데이터는 예시 입니다.
# """ 사이의 데이터를 지우고 넣으시면 됩니다.

b = b.split("\n")
    
num = []
name = []

for i in range(len(b)):
    if "Bronze" in b[i] or "Silver" in b[i]or "Gold" in b[i] or "Platinum" in b[i] or "Diamond" in b[i]  or "Ruby" in b[i]:
        k = b[i].split()
        num.append(k[2])
        name.append(b[i+1])
        
    elif "Sprout" in b[i]:
        k = b[i].split()
        num.append(k[1])
        name.append(b[i+1])  

lst = []
no_lst = []

converter = [0] * len(num)

while 1:
    try:
        c =  input()

        if c == "0":
            break
        
        n = num.index(c)
        st = num[n] + " " + name[n]
        print(f"{st}.py")
        
        if st in lst:
            continue
        else:
            lst.append(st)
        
    except:
        print(f"\n[ {c} ] 는 목록에 없습니다. 다시 입력해주세요.\n")
        continue

print("\n\n> 검색 기록 --------\n\n")

for i in lst:
    print(i)

print("\n\n> 검색 되지 않음 ---- \n\n")

for i in range(len(num)):
    for j in lst:
        if num[i] in j:
            converter[i] += 1
            
for i in range(len(converter)):
    if converter[i] == 0:
        print(f"{num[i]} {name[i]}")

