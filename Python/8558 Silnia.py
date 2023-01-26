n = int(input())

fac = 1

for i in range(1, n+1):

    fac = fac * i

fac = str(fac)

print(fac[len(fac)-1 : ])
