import sys

loop = int(input())

vals = []
for _ in range(loop):
    vals.append(int(sys.stdin.readline()))

vals.sort()                 # 1 2 3 4 5
for k in vals:
    print(k)

#vals                       # 5 2 3 4 1
#vals.sort(reverse=True)    # 5 4 3 2 1
#vals.reverse()              # 1 4 3 2 5
#print(vals)