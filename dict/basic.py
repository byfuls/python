
### 딕셔너리 생성 {} ###
#dictVariable = {}
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {}

### 딕셔너리 생성 {} ###
#dictVariable = {
#    "monday": "아 출근하기 싫음",
#    "tuesday": "아직도 멍~한상태",
#    "wednesday": "그래도 반 지났으니 힘내자",
#    "tursday": "내일이면 금요일이야!!!",
#    "friday": "불금불금불금 으아아아!",
#    "saturday": "왘! 토요일이니 마지막으로 불태워보자!!",
#    "sunday": "푸우욱..쉬면서..내일을 맞이할...앜.."
#}
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'monday': '아 출근하기 싫음', 'tuesday': '아직도 멍~한상태', 'wednesday': '그래도 반 지났으니 힘내자', 'tursday': '내일이면 금요일이야!!!', 'friday': '불금불금불금 으아아아!', 'saturday': '왘! 토요일이니 마지막으로 불태워보자!!', 'sunday': '푸우욱..쉬면서..내일을 맞이할...앜..'}

### 딕셔너리 변환 dict() - 리스트 ###
#listVariable = [('a', 'b'), ('c', 'd'), ('e', 'f')]
#dictVariable = dict(listVariable)
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'a': 'b', 'c': 'd', 'e': 'f'}

#listVariable = ['ab', 'cd', 'ef']
#dictVariable = dict(listVariable)
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'a': 'b', 'c': 'd', 'e': 'f'}


### 딕셔너리 변환 dict() - 튜플 ###
#tupleVariable = (['a', 'b'], ['c', 'd'], ['e', 'f'])
#dictVariable = dict(tupleVariable)
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'a': 'b', 'c': 'd', 'e': 'f'}
#
#tupleVariable = ('ab', 'cd', 'ef')
#dictVariable = dict(tupleVariable)
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'a': 'b', 'c': 'd', 'e': 'f'}

### 딕셔너리 추가 ###
#dictVariable = {'a':1, 'b':2, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'd': 4}
#dictVariable['c'] = 3
#print(dictVariable)         # {'a': 1, 'b': 2, 'd': 4, 'c': 3}

### 딕셔너리 수정 ###
#dictVariable = {'a':1, 'b':2, 'c':5, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 5, 'd': 4}
#dictVariable['c'] = 3
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#dictVariable1 = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable1)         # {'a': 1, 'b': 2, 'c': 5, 'd': 4}
#dictVariable2 = {'c':7, 'e':5, 'f':6, 'g':7}
#print(dictVariable2)         # {'c': 7, 'e': 5, 'f': 6, 'g': 7}
#
#dictVariable1.update(dictVariable2)
#print(dictVariable1)         # {'a': 1, 'b': 2, 'c': 7, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

### 딕셔너리 삭제 ###
#dictVariable = {'a':1, 'b':2, 'z':9, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'z': 9, 'c': 3, 'd': 4}
#del dictVariable['z']

#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#dictVariable.clear()
#print(dictVariable)         # {}

### 딕셔너리 in 키 확인 ###
#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#check = 'c' in dictVariable
#print(check)                # True

### 딕셔너리 키 확인, keys() ###
#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#keys = dictVariable.keys()
#print(keys)                 # dict_keys(['a', 'b', 'c', 'd'])

### 딕셔너리 값 ###
#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#value = dictVariable['b']
#print(value)                # 2
#
#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#value = dictVariable.get('c')
#print(value)                # 3

#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#values = dictVariable.values()
#print(values)               # dict_values([1, 2, 3, 4])

#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#keyValues = dictVariable.items()
#print(keyValues)            # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#tmpDict = dictVariable
#tmpDict['c'] = "changed"
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 'changed', 'd': 4}

dictVariable = {'a':1, 'b':2, 'c':3, 'd':4}
print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
tmpDict = dictVariable.copy()
tmpDict['c'] = "changed"
print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
