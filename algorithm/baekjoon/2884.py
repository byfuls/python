h, m = map(int, input().split())

dh = 0
dm = 0
if 45 > m:
    dh = h - 1
    dm = 60 + m - 45
else:
    dh = h
    dm = m - 45

if 0 > dh:
    dh = 23

print(dh, dm)

