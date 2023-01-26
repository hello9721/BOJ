l = int(input())
m = int(input())

o = m - l

if o <= 0: print("Congratulations, you are within the speed limit!")
else:

    f = 0
    
    if o < 21: f = 100
    elif o < 31: f = 270
    else: f = 500

    print(f"You are speeding and your fine is ${f}.")
