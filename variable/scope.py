

#def func(x):
#    print(x)
#
#func(1)   # 1

#def func(x):
#    print(x)    # 1
#    print(y)    # NameError: name 'y' is not defined
#
#func(1)

#y = 2
#def func(x):
#    print(x)    # 1
#    print(y)    # 2
#
#func(1)

#y = 2
#def func(x):
#    print(x)    # 1
#    print(y)    # UnboundLocalError: local variable 'y' referenced before assignment
#    y = 20
#
#func(1)

y = 2
def func(x):
    global y
    print(x)    # 1
    print(y)    # 2
    y = 20
    print(y)    # 20

func(1)
