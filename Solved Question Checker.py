# mode 1 : solved.ac 에서 복사 해올 때

def solved(b):
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

    return num, name

# mode 2 : '문제번호 타이틀\n' 로 이루어진 목록이 있을 때
# 출력되는 검색 목록이나 검색 되지 않음 목록을 재사용해도 된다.

def search(b):
    b = b.strip().split("\n")

    num = []
    name = []

    for i in b:
        lst = i.split(" ", 1)
        if (lst[0].isdigit()):
            num.append(lst[0])
            name.append(lst[1])

    return num, name

# 만들어진 리스트에서 검색
# 문제 번호를 입력 => '문제번호 타이틀.확장자' 출력
# 0을 입력하면 이때까지의 검색 목록과 검색하지 않은 목록이 출력된다.

def list_print(num, name):
    lst = []
    no_lst = []
    e = input("\n사용하시는 확장자를 입력해주세요\n\n>> ")

    print("\n\n문제 번호만 검색해주세요\n\n")
    
    converter = [0] * len(num)

    while 1:
        try:
            c =  input()

            if c == "0":
                break
            
            n = num.index(c)
            st = num[n] + " " + name[n]
            print(f"{st}.{e}")
            
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




b = """
0000 data
"""

# 위의 데이터는 예시 입니다.
# 지우고 넣으시면 됩니다.

mode_checker = input()

if mode_checker == '1':
    num, name = solved(b)
    list_print(num, name)
elif mode_checker == '2':
    num, name = search(b)
    list_print(num, name)
else:
    print(">\t'1' 혹은 '2'로 입력해주세요.")

