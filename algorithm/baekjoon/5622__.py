#numberMap = {}
#numberMap['ABC'] = [2, 3]
#numberMap['DEF'] = [3, 4]
#numberMap['GHI'] = [4, 5]
#numberMap['JKL'] = [5, 6]
#numberMap['MNO'] = [6, 7]
#numberMap['PQRS'] = [7, 8]
#numberMap['TUV'] = [8, 9]
#numberMap['WXYZ'] = [9, 10]
#
#strs = numberMap.keys()
#
#inputStr = input()
#time = 0
#for s in inputStr:
#    for k in strs:
#        if k.find(s) > 0:
#            time += numberMap[k][1]
#
#print(time)

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
inputData = input()
time = 0
for idx in range(len(inputData)):
    for ch in dial:
        if inputData[idx] in ch:
            time += (dial.index(ch)+1)+2

print(time)