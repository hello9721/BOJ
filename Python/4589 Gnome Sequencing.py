t = int(input())

print("Gnomes:")

for i in range(t):

    a, b, c = map(int, input().split())

    if (a > b) & (b > c): print("Ordered")
    elif (c > b) & (b > a): print("Ordered")
    else : print("Unordered")
