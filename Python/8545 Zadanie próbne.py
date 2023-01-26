W = input()
lst = []

for i in range(len(W)):
    lst.append(W[len(W)- i - 1])

print("".join(lst))
