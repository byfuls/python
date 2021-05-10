import sys

loop = int(input())

for _ in range(loop):
    many, idx = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    watch = idx
    count = 0
    while True:
        maxPri = max(arr)
        if arr[0] >= maxPri:
            count+=1
            if watch == 0:
                print(count)
                break
            else:
                arr.pop(0)
        else:
            arr.append(arr.pop(0))

        if 0 == watch:
            watch = len(arr)-1
        else:
            watch -= 1