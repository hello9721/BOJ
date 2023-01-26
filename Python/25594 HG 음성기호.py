# 1 시간초과

##import sys as s
##
##HG = ["aespa", "baekjoon", "cau", "debug", "edge", "firefox", "golang", "haegang", "iu", "java", "kotlin", "lol", "mips", "null", "os", "python", "query", "roka", "solvedac", "tod", "unix", "virus", "whale", "xcode", "yahoo", "zebra"]
##
##s = s.stdin.readline()
##st = ""
##
##while 1:
##
##    n = ord(s[0]) - 97
##
##    if HG[n] in s:
##
##        st += s[0]
##        s = s[len(HG[n]): ]
##
##    else:
##        
##        print("ERROR!")
##        break
##
##    if s == "\n":
##
##        print("It's HG!")
##        print(f"{st}")
##        break

import sys as s

HG = ["aespa", "baekjoon", "cau", "debug", "edge", "firefox", "golang", "haegang", "iu", "java", "kotlin", "lol", "mips", "null", "os", "python", "query", "roka", "solvedac", "tod", "unix", "virus", "whale", "xcode", "yahoo", "zebra"]

s = s.stdin.readline()
st = s

for i in range(26):

    if HG[i] in s:

        s = s.replace(HG[i], "*")
        st = st.replace(HG[i], HG[i][0])

s = set(s.strip())

if (s == {"*"}) & (st != "\n"):

    print("It's HG!")
    print(st)

else: print("ERROR!")
