from srctarget import globalvar

print('flow - 1')

def imcalled():
    print(f'hi, I am called')

def globalcalled():
    global globalvar
    tmp = globalvar
    print(tmp)

print('flow - 2')
