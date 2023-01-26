s = int(input())
n = 1
sum_n = 0

while sum_n < s:

    sum_n += n
    n += 1

if sum_n == s : print(n-1)
elif sum_n > s : print(n-2)

    
