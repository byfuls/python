loop = int(input())
valArr = input()

arr = [int(s) for s in valArr]

sumVal = 0
for i in range(loop):
    sumVal += arr[i]

print(sumVal)