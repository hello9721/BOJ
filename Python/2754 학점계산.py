grade = [ 4, 3, 2, 1 ]
score = [ 0.3, 0.0, -0.3]

check = [ [ "A", "B", "C", "D" ], [ "+", "0", "-" ] ]

t = input()

if t != "F":
    t = list(t)
    print( grade[check[0].index(t[0])] + score[check[1].index(t[1])])
else: print(0.0)
