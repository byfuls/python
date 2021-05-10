n = int(input())

valList = [0, 1]
for i in range(2, n+1):
    val = valList[i-1] + valList[i-2]
    valList.append(val)

print(valList[n])