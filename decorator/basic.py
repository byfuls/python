
def decoFunc(func):
    def newFunc(*args, **kwargs):
        print('[decoFunc] decoration function name: ', func.__name__)
        print('[decoFunc] position arguments: ', args)
        print('[decoFunc] keyword arguments: ', kwargs)
        return func(*args, **kwargs)
    return newFunc

def decoOther(func):
    def newFunc(*args, **kwargs):
        print('[decoOther] decoration function name: ', func.__name__)
        print('[decoOther] position arguments: ', args)
        print('[decoOther] keyword arguments: ', kwargs)
        return func
    return newFunc

# 수동으로 데커레이터 적용
#def over10value(a):
#    return "10 이상 값입니다" if a > 10 else "10 미만 값입니다"
#
#calc = decoFunc(over10value)
#print("result: ", calc(9))

# 데커레이터를 통해 적용
#@decoFunc
#def over10value(a):
#    return "10 이상 값입니다" if a > 10 else "10 미만 값입니다"
#
#print("result: ", over10value(9))

#________________________________________________________________
#def decoAppFunc(func):
#    def newFunc(*args, **kwargs):
#        if (args[0] % 2) != 0:
#            return "짝수만 검사합니다"
#        else:
#            return func(*args, **kwargs)
#    return newFunc
#
#@decoAppFunc
#def over10value(a):
#    return "10 이상 값입니다" if a > 10 else "10 미만 값입니다"
#
#print("result: ", over10value(9))   # 짝수만 검사합니다
#print("result: ", over10value(8))   # 10 미만 값입니다
#________________________________________________________________

def decoFunc_1(func):
    def newFunc(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return newFunc

def decoFunc_2(func):
    def newFunc(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + result
    return newFunc

@decoFunc_1
@decoFunc_2
def plusOne(val):
    return val+1

print("result: ", plusOne(3))   # 64

