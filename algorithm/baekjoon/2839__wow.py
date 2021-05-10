sugar = int(input())

bagCount = 0
while True:
    if sugar % 5 == 0:
        bagCount += int(sugar / 5)
        print(bagCount)
        break
    else:
        sugar -= 3
        bagCount += 1
        if 0 > sugar:
            print(-1)
            break