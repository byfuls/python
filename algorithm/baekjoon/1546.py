
count = int(input())
tarr = list(map(int, input().split()))
arr = []
for i in range(count):
    arr.append(tarr[i])

maxValue = max(arr)

newArr = []
for k in arr:
    newArr.append(k/maxValue*100)
print(sum(newArr)/count)