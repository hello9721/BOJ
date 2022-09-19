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
                
            elif write_mode == '2' :
                file = open("./BOJ_list.txt", "a")

            file.write("검색 기록 -------- \n\n")
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
2558 A+B - 2
2562 최댓값
2577 숫자의 개수
2588 곱셈
2675 문자열 반복
2738 행렬 덧셈
2739 구구단
2741 N 찍기
2742 기찍 N
2743 단어 길이 재기
2744 대소문자 바꾸기
2753 윤년
2754 학점계산
2884 알람 시계
2908 상수
2920 음계
2941 크로아티아 알파벳
3003 킹, 퀸, 룩, 비숍, 나이트, 폰
3046 R2
3052 나머지
3733 Shares
4101 크냐?
4344 평균은 넘겠지
4999 아!
5337 웰컴
5338 마이크로소프트 로고
5339 콜센터
5522 카드 게임
5597 과제 안 내신 분..?
5622 다이얼
7287 등록
8393 합
8958 OX퀴즈
9086 문자열
9498 시험 성적
10171 고양이
10172 개
10430 나머지
10699 오늘 날짜
10718 We love kriii
10807 개수 세기
10809 알파벳 찾기
10818 최소, 최대
10869 사칙연산
10871 X보다 작은 수
10872 팩토리얼
10926 ??!
10950 A+B - 3
10951 A+B - 4
10952 A+B - 5
10998 A×B
11021 A+B - 7
11022 A+B - 8
11382 꼬마 정민
11654 아스키 코드
11718 그대로 출력하기
11720 숫자의 합
14681 사분면 고르기
15552 빠른 A+B
15733 나는 누구인가
15964 이상한 기호
18108 1998년생인 내가 태국에서는 2541년생?!
25083 새싹
25304 영수증
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

