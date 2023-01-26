# 1
# 72ms
# 30840KB

n = 90
score = int(input())

if score >= n: print("A")
elif score >= n - 10: print("B")
elif score >= n - 20: print("C")
elif score >= n - 30: print("D")
else: print("F")


# 2
# 68ms
# 30840KB

n = 90
score = int(input())
grade = [ "A","B","C","D" ]

for i in range(0, 40, 10):
    if score >= n - i:

        print(grade[i//10])
        break
    
    elif score < 60:

        print("F")
        break
