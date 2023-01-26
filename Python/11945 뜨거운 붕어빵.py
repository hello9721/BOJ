n, m = map(int, input().split())

for i in range(n):

    a = input()

    for j in range(m): print(a[m-j-1], end="")
        
    print("")
