
inputData = list(input().split())

arr = []
for v in inputData:
    tmp = v[::-1]
    arr.append(int(tmp))

print(max(arr))