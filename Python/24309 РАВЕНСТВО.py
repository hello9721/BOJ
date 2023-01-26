# a*x = b-c 일 때 abc를 입력받고 x를 출력하라.

a = int(input())
b = int(input())
c = int(input())

n = b-c

if n%a == 0: print(n//a)
else: print(n/a)
