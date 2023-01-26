h, m, s = map(int, input().split())
t = int(input())

m = m + (t//60)
s = s + t%60

if s >= 60:
    
    m = m + (s//60)
    s = s%60
    
if m >= 60:
    
    h = h + (m//60)
    m = m%60
    
if h >= 24:
    
    h = h%24
    
print(h, m, s)
