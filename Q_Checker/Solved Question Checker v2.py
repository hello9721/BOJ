from urllib.request import urlopen as u
from bs4 import BeautifulSoup as b

check_li = []

while 1:
    
    try:
        
        q = input("번호를 입력해주세요. ( 종료는 e )\n>> ")

        if q.lower() == "e" :

            print("")
            for i in check_li: print(i)
            print("")
            
            print("\n종료합니다.")
            break

        html = u(f"https://www.acmicpc.net/problem/{q}")
        ob = b(html, "html.parser")

        num = ob.body.find("span", {"id":"problem_title"})

        print("")
        print(f"{q} {num.text}")
        check_li.append(f"{q} {num.text}")
        print("")

    except:

        print("\n다시 입력해주세요.\n")
        continue
        
