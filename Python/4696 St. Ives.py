while 1:

    t = float(input())

    if t == 0: break

    n = 1 + t + (t * t) + (t * t * t) + (t * t * t * t)

    print(f"{n:.2f}")
    
