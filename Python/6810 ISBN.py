a = [0] * 3

for i in range(3):

    a[i] = int(input())
    
    if i%2 == 1: a[i] = a[i]*3

print(f"The 1-3-sum is {sum(a)+91}")
