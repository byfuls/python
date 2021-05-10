loop, num = map(int, input().split())

arr = [i for i in range(1, loop+1)]
jump = num-1
result = []
while len(arr) > 0:
    if jump >= len(arr):
        jump = jump % len(arr)
    else:
        result.append(str(arr.pop(jump)))
        jump = (jump + num) - 1

print("<", ", ".join(result), ">", sep='')