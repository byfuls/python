inputData = input().upper()
searchKeys = list(set(inputData))

countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))

if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])