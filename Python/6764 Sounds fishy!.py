depth = [0] * 4

for i in range(4): depth[i] = int(input())

if depth[3] > depth[2] > depth[1] > depth[0]: print("Fish Rising")
elif depth[0] > depth[1] > depth[2] > depth[3]: print("Fish Diving")
elif depth[3] == depth[2] == depth[1] == depth[0]: print("Fish At Constant Depth")
else: print("No Fish")
