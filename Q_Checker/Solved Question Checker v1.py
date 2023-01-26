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
            st = num[i] + " " + name[i]
            
            no_lst.append(st)
            print(st)
            
    return lst, no_lst

# 목록 저장하기
# 현재 작업 디렉토리에 BOJ_list.txt 라는 이름으로 저장됩니다.

def save(lst, nlst):
    save = input("\n\n리스트를 저장하시겠습니까? ( Y / N )\n\n>> ")

    if save.upper() == "Y":
    
        write_mode = input("\n저장 모드를 선택해주세요. ( NEW => 1 / CONTINUE => 2 )\n\n>> ")

        if (write_mode == '1') | (write_mode == '2'):
            
            if write_mode == '1' :
                file = open("./BOJ_list.txt", "w")
                file.write("검색 기록 -------- \n\n")
                
            elif write_mode == '2' :
                file = open("./BOJ_list.txt", "a")
                file.write("\n\n검색 기록 -------- \n\n")

            for i in lst:
                file.write(f"{i}\n")
                
            file.write("\n\n검색 되지 않음 ---- \n\n")
            for i in nlst:
                file.write(f"{i}\n")
                
            file.close()

            print("\n저장되었습니다.\n\n")
            
        else:
           print(">\t'1' 혹은 '2'로 입력해주세요.") 
    else:
        print("\n종료합니다.\n\n")
        

    


b = """
0000 data
"""

# 위의 데이터는 예시 입니다.
# 지우고 넣으시면 됩니다.

mode_checker = input("\n모드를 선택해주세요. ( 1 / 2 )\n\n>> ")

if mode_checker == '1':
    num, name = solved(b)
    lst, nlst = list_print(num, name)
    save(lst, nlst)
elif mode_checker == '2':
    num, name = search(b)
    lst, nlst = list_print(num, name)
    save(lst, nlst)
else:
    print(">\t'1' 혹은 '2'로 입력해주세요.")

