
arr = []
for i in range(10):
    v = int(input())
    arr.append(v % 42)
setArr = set(arr)
print(len(setArr))