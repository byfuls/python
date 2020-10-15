
sortedList = ['CONID', 1234, 321, 123]
print(sortedList)

sortedDict = {
	"conid": sortedList[0],
	"test": sortedList[1]
}
print(sortedDict)


keyList = ['conid', 'var1', 'var2', 'var3']
result = dict(zip(keyList, sortedList))
print(result)
