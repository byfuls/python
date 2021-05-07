
x,y,z = 0, 0, 0
for i in range(3):
    if i == 0:
        x = int(input())
    elif i == 1:
        y = int(input())
    else:
        z = int(input())

val = x * y * z
arr = [int(k) for k in str(val)]

for i in range(0, 9+1):
    print(arr.count(i))