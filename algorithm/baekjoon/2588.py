x = int(input())
y = int(input())
yy = [int(t) for t in str(y)]

for v in reversed(yy):
    print(x*v)
print(x*y)