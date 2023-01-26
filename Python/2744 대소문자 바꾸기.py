t = input()

for i in range(len(t)):
    if t[i].isupper() : print(t[i].lower(), end = "")
    else: print(t[i].upper(), end = "")

print("")
