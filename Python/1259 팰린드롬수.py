# 앞에서 읽든 뒤에서 읽든 똑같은 수
# 마지막 입력 0

# 팰린드롬수 면 yes, 아니면 no

while 1:

    n = input()
    if n == "0": break

    back_list = ["a"] * len(n)
    cnt = len(n) - 1

    for i in n:
        
        back_list[cnt] = i
        cnt -= 1
    
    if n == "".join(back_list): print("yes")
    else: print("no")