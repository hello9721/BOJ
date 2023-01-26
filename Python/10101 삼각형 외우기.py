a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60: print("Equilateral")
elif (a + b + c == 180) & ((a == b) | (b == c) | (a == c)): print("Isosceles")
elif a + b + c == 180: print("Scalene")
else: print("Error")
