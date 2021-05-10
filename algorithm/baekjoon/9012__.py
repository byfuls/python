import sys

loop = int(input())

for _ in range(loop):
    vpsArr = list(sys.stdin.readline().strip())       # strip() : return as string
    while len(vpsArr):
        head = vpsArr.pop(0)
        if head == "(":
            try:
                tail = vpsArr.index(")")
                if tail >= 0:
                    del vpsArr[tail]
                    continue
            except:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("YES")