while 1:

    l = input()

    if l == "END": break
    
    for i in range(len(l) - 1, 0, -1): print(l[i], end = "")

    print(l[0])
