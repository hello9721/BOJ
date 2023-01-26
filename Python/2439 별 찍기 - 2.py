n = int(input())

for i in range(n):
    
    s = 1
    s += i

    print(f"{' '*(n-s)}{'*'*s}")

