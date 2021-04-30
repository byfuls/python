
### list comprehension ###

# [기존방식] 1. 하나씩 대입하기
listVar = []
listVar.append(1)
listVar.append(2)
listVar.append(3)
listVar.append(4)
listVar.append(5)
print(listVar)      # [1, 2, 3, 4, 5]

# [기존방식] 2. 이터레이터 + range() 함수를 활용해서 대입하기
listVar = []
for var in range(1, 6):
    listVar.append(var)
print(listVar)      # [1, 2, 3, 4, 5]

# [기존방식] 3. list() 함수 + range() 함수를 활용해서 대입하기
listVar = list(range(1,6))
print(listVar)      # [1, 2, 3, 4, 5]

# [리스트 컴프리핸션] 1. 기본
listVar = [var for var in range(1,6)]
print(listVar)      # [1, 2, 3, 4, 5]

# [리스트 컴프리핸션] 2. 응용 (2의 배수 만들기)
listVar = [var * 2 for var in range(1,6)]
print(listVar)      # [2, 4, 6, 8, 10]

# [리스트 컴프리핸션] 3. 응용 (홀수 만들기)
listVar = [var for var in range(1,6) if var % 2 == 1]
print(listVar)      # [1, 3, 5]

# [리스트 컴프리핸션] 3. 응용 ((x,y) => x는 1~3, y는 1~5까지의 가지의 수를 리스트로 모두 출력)
xVar = range(1,4)
yVar = range(1,6)
xyList = [[x, y] for x in xVar for y in yVar]
for xy in xyList:
    print(xy)
# 튜플로 출력
xyTuple = [(x, y) for x in xVar for y in yVar]
for xy in xyTuple:
    print(xy)

word = 'letters'
print(word.count(letter))
