while 1:

    t = ['a', 'e', 'i', 'o', 'u']
    s = list(input().lower())

    cnt = 0
    
    for i in t:

        if i in s: cnt += s.count(i)
    
    if '#' in s: break
    else: print(cnt)
    
