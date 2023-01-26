l, p = map(int, input().split())
lst = list(map(int, input().split()))

n = l * p

for i in lst: print(i-n, end = " ")
