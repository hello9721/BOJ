N, M = map(int, input().split())

n, m = (N-1),(M-1)

a = n + ( N * m )
b = m + ( M * n )

print(min(a,b))
