lst = [0] * 9

for i in range(9):
    lst[i] = int(input())

print( max(lst), lst.index(max(lst))+1 )
