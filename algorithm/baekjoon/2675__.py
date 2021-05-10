
loop = int(input())

for _ in range(loop):
    inputData = input().split()
    loop = int(inputData.pop(0))
    data = inputData.pop(0)
    result = ''
    for s in data:
        result += s*loop
    print(result)