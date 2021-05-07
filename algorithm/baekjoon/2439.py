loop = int(input())

for v in range(1, loop+1):
    space = ' ' * (loop-v)
    star = '*' * v
    print(space + star)