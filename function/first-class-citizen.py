
def printFunc():
    print("hello world")

def runFunc(func):
    func()

runFunc(printFunc)

print(type(printFunc))  # <class 'function'>
print(type(runFunc))    # <class 'function'>

print("_____________________________")

def sumFunc(*args):
    return sum(args)

def runFunc(func, *args):
    return func(*args)

print(type(sumFunc))    # <class 'function'>
print(type(runFunc))    # <class 'function'>

result = runFunc(sumFunc, 1,2,3,4,5,6,7,8,9,10)
print(type(result))     # <class 'int'>
print(result)           # 55
