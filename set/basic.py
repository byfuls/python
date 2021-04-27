
### 셋 생성 ###
#setVariable = set()
#print(type(setVariable))   # <class 'set'>
#print(setVariable)         # set()
#
#setVariable = {1,2,3,4,5}
#print(type(setVariable))   # <class 'set'>
#print(setVariable)         # {1, 2, 3, 4, 5}

### dict 생성 - set과 비교 ###
#dictVariable = {'a': 1, 'b': 2, 'c': 3}
#print(type(dictVariable))   # <class 'dict'>
#print(dictVariable)         # {'a': 1, 'b': 2, 'c': 3}

### set 변환 - 문자열 to 셋 ###
#stringVar = "message"
#setVariable = set(stringVar)
#print(type(setVariable))        # <class 'set'>
#print(setVariable)              # {'g', 's', 'e', 'm', 'a'}
#sortedSetVariable = sorted(setVariable)
#print(type(sortedSetVariable))  # <class 'list'>
#print(sortedSetVariable)        # ['a', 'e', 'g', 'm', 's']

### set 변환 - 리스트 to 셋 ###
#listVar = ['a1', 'b2', 'c3', 'd4']
#setVar = set(listVar)
#print(type(setVar))        # <class 'set'>
#print(setVar)              # {'c3', 'd4', 'b2', 'a1'}

### set 변환 - 튜플 to 셋 ###
#tupleVar = ('a1', 'b2', 'c3', 'd4')
#setVar = set(tupleVar)
#print(type(setVar))        # <class 'set'>
#print(setVar)              # {'c3', 'd4', 'a1', 'b2'}

### set 변환 - 딕셔너리 to 셋 ###
#dictVar = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#setVar = set(dictVar)
#print(type(setVar))        # <class 'set'>
#print(setVar)              # {'b', 'd', 'a', 'c'}

### 콤비네이션과 연산자 ###
#foods = {
#    '라면' : {'면', '스프', '물', '계란'},
#    '김치찌개' : {'물', '김치', '고기'},
#    '부대찌개' : {'물', '스팸', '고기', '면'},
#    '된장찌개' : {'물', '된장', '두부'}
#}
#
#for food, list in foods.items():
#    if '물' in list:
#        print(food)
#        # 라면
#        # 김치찌개
#        # 부대찌개
#        # 된장찌개

#foods = {
#    '라면' : {'면', '스프', '물', '계란'},
#    '김치찌개' : {'물', '김치', '고기'},
#    '부대찌개' : {'물', '스팸', '고기', '면'},
#    '된장찌개' : {'물', '된장', '두부'}
#}
#
#for food, list in foods.items():
#    if list & {'고기', '면'}:
#        print(food)
#        # 라면
#        # 김치찌개
#        # 부대찌개

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food & B_food))    # <class 'set'>
#print(A_food & B_food)          # 물, 면
#print(type(A_food.intersection(B_food)))    # <class 'set'>
#print(A_food.intersection(B_food))          # 물, 면

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food | B_food))    # <class 'set'>
#print(A_food | B_food)          # {'면', '스팸', '스프', '물', '계란', '고기'}

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food - B_food))    # <class 'set'>
#print(A_food - B_food)          # {'스프', '계란'}

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food ^ B_food))    # <class 'set'>
#print(A_food ^ B_food)          # {'계란', '스팸', '고기', '스프'}

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food <= B_food))    # <class 'bool'>
#print(A_food <= B_food)          # False
#print(type(A_food.issubset(B_food)))    # <class 'bool'>
#print(A_food.issubset(B_food))          # False
#
#A_food = {'면', '물'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food <= B_food))    # <class 'bool'>
#print(A_food <= B_food)          # True
#print(type(A_food.issubset(B_food)))    # <class 'bool'>
#print(A_food.issubset(B_food))          # True

#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food >= B_food))    # <class 'bool'>
#print(A_food >= B_food)          # False
#print(type(A_food.issuperset(B_food)))    # <class 'bool'>
#print(A_food.issuperset(B_food))          # False
#
#A_food = {'물', '스팸', '고기', '면'}
#B_food = {'면', '물'}
#print(type(A_food >= B_food))    # <class 'bool'>
#print(A_food >= B_food)          # True
#print(type(A_food.issuperset(B_food)))    # <class 'bool'>
#print(A_food.issuperset(B_food))          # True


#A_food = {'면', '스프', '물', '계란'}
#B_food = {'물', '스팸', '고기', '면'}
#print(type(A_food > B_food))    # <class 'bool'>
#print(A_food > B_food)          # False
#
#A_food = {'물', '스팸', '고기', '면'}
#B_food = {'면', '물'}
#print(type(A_food > B_food))    # <class 'bool'>
#print(A_food > B_food)          # True

#A_food = {'면', '스프', '물', '계란'}
#print(A_food)

### 셋 항목 추가 ###
#A_food = {'면', '스프', '물', '계란'}
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면', '계란'}
#A_food.add('대파')
#A_food.add('고추')
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'고추', '대파', '계란', '면', '스프', '물'}

### 셋 항목 결합 ###
#A_food = {'면', '스프', '물', '계란'}
#print(type(A_food))         # <class 'set'>
#print(A_food)               # {'물', '스프', '면', '계란'}
#B_food = {'대파', '고추'}   # <class 'set'>
#A_food.update(B_food)
#print(type(A_food))         # <class 'set'>
#print(A_food)               # {'물', '대파', '고추', '면', '계란', '스프'}
#C_food = ['치즈', '떡', '김치'] # <class 'list'>
#A_food.update(C_food)
#print(type(A_food))         # <class 'set'>
#print(A_food)               # {'계란', '고추', '떡', '치즈', '물', '면', '대파', '김치', '스프'}

### 셋 항목 삭제 ###
## remove
#A_food = {'면', '스프', '물', '계란'}
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면', '계란'}
#A_food.remove('계란')
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면'}
#A_food.remove('계란')   # KeyError: '계란'
#
## discard
#A_food = {'면', '스프', '물', '계란'}
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면', '계란'}
#A_food.discard('계란')
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면'}
#A_food.discard('계란')
#print(type(A_food))     # <class 'set'>
#print(A_food)           # {'물', '스프', '면'}

### 셋 항목 복사 ###
A_food = {'면', '스프', '물', '계란'}
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '면', '계란', '스프'}
B_food = A_food.copy()
print(type(B_food))     # <class 'set'>
print(B_food)           # {'물', '면', '계란', '스프'}

A_food.discard('계란')
print(type(A_food))     # <class 'set'>
print(A_food)           # {'물', '면', '스프'}
print(type(B_food))     # <class 'set'>
print(B_food)           # {'물', '면', '계란', '스프'}
