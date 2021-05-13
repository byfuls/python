import sys

loop = int(input())
vals = []
for _ in range(loop):
    vals.append(int(sys.stdin.readline()))
vals.sort()

def average(vals):
    return round(sum(vals)/len(vals))

def center(vals):
    return vals[len(vals)//2]

def freq(vals):
    import collections
    tmp = collections.Counter(vals).most_common()

    if len(tmp) > 1:
        if tmp[0][1] == tmp[1][1]:
            return tmp[1][0]
        else:
            return tmp[0][0]
    else:
        return tmp[0][0]

def range(vals):
    return vals[len(vals)-1] - vals[0]

print(average(vals))
print(center(vals))
print(freq(vals))
print(range(vals))