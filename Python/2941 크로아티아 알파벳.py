t = input()

end = [ "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" ]

for i in end: t = t.replace(i, "*")

print(len(t))
