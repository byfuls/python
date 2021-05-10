
count = int(input())
valList = map(int, input().split())

found = 0
for val in valList:
    if val > 1:
        passFlag = False
        for i in range(2, val):
            if val % i == 0:
                passFlag = True
                break
        if passFlag is False:
            found += 1

print(found)