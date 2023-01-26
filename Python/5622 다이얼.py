phone = [ "-","-","-","ABC","DEF","GHI","JKL","MNO","PQRS","TUV", "WXYZ" ]
word = input()

time = 0

for i in word:
    for j in range(11):
        if i in phone[j]:
            time += j

print(time)
