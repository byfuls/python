


### 튜플 생성 () ###
#tupleVariable = ()
#print(tupleVariable)    # ()

### 튜플 생성, 하나의 요소 ###
#tupleVariable = 'tupleData1'
#print(type(tupleVariable))      # <class 'str'>
#print(tupleVariable)            # tupleData1
#
#tupleVariable = 'tupleData1',
#print(type(tupleVariable))      # <class 'tuple'>
#print(tupleVariable)            # ('tupleData1',)

### 튜플 생성, 두개 이상의 요소 ###
#tupleVariable = 'tupleData1', 'tupleData2'
#print(type(tupleVariable))      # <class 'tuple'>
#print(tupleVariable)            # ('tupleData1', 'tupleData2')
#
#tupleVariable = ('tupleData3', 'tupleData4')
#print(type(tupleVariable))      # <class 'tuple'>
#print(tupleVariable)            # ('tupleData3', 'tupleData4')

### 튜플 언패킹 ###
#tupleVariable1, tupleVariable2, tupleVariable3 = ('data1', 'data2', 'data3')
#print(type(tupleVariable1))      # <class 'str'>
#print(tupleVariable1)            # data1
#print(type(tupleVariable2))      # <class 'str'>
#print(tupleVariable2)            # data2
#print(type(tupleVariable3))      # <class 'str'>
#print(tupleVariable3)            # data3

### 튜플로 변환 (tuple()) ###
listVariable = ['listData1', 'listData2', 'listData3']
tupleVariable = tuple(listVariable)

print(type(listVariable))       # <class 'list'>
print(listVariable)             # ['listData1', 'listData2', 'listData3']
print(type(tupleVariable))      # <class 'tuple'>
print(tupleVariable)            # ('listData1', 'listData2', 'listData3')
