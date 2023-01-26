# 아스키 코드 영어 소문자 10진수 코드 97 ~ 122

word = list(input())

for i in range(97, 123):

    count = -1
    
    for j in word:
        
        if i == ord(j): count = word.index(j)

    print(count, end = " ")
