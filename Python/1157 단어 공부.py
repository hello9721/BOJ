word = input().upper()

st = list(set(word))
lst = [0] * len(st)

for i in st: lst[st.index(i)] = word.count(i)
    
m = max(lst)

if lst.count(m) == 1: print(st[lst.index(m)].upper())
    
else: print("?")
