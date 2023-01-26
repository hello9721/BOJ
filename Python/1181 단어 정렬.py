t = int(input())

word = [0] * t

for i in range(t):
    temp = input()

    word[i] = [len(temp), temp]

word.sort()

for i in range(t):
    if i == 0:
        print(word[i][1])
    elif word[i][1] == word[i-1][1]:
        continue
    else:
        print(word[i][1])
