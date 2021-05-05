
def stackAdd():
    totalValue = 0
    stackCount = 0
    def add(value):
        nonlocal totalValue, stackCount
        stackCount += 1
        totalValue += value
        return totalValue, stackCount
    return add

add = stackAdd()
print(add(3))   # (3, 1)
print(add(2))   # (5, 2)
