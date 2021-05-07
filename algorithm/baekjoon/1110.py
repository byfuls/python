
v = int(input())
ar = [int(k) for k in str(v)]
if 1 >= len(ar):
    ar.append(ar[0])
    ar[0] = 0

count = 1
left = ar.copy()
right = [0, 0]
while True:
    try:
        tmpVal = left[0] + left[1]
        if 10 > tmpVal:
            right[0] = 0
            right[1] = tmpVal
        else:
            right = [int(k) for k in str(tmpVal)]

        left[0] = left[1]
        left[1] = right[1]

        if ar == left:
            break
        else:
            count+=1
    except:
        break

print(count)