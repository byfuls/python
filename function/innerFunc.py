
def outerFunc():
    x = 1
    def innerFunc():
        nonlocal x
        x = 2
    innerFunc()
    print(x)

outerFunc()