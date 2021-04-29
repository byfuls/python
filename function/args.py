
# 일반적인 인자 전달
# O
def userInfo(name, phone, address):
    return {'이름': name, '전화번호':phone, '주소':address}

user = userInfo('김말똥', '01012341234', '123-123')
print(type(user))   # <class 'dict'>

# X
def userInfo(name, phone, address):
    return {'이름': name, '전화번호':phone, '주소':address}

user = userInfo('01012341234', '123-123', '김말똥')
print(type(user))   # <class 'dict'>
print(user)         # {'이름': '01012341234', '전화번호': '123-123', '주소': '김말똥'}

# 키워드를 통한 인자 전달
def userInfo(name, phone, address):
    return {'이름': name, '전화번호':phone, '주소':address}

user = userInfo(phone='01012341234', address='123-123', name='김말똥')
print(type(user))   # <class 'dict'>
print(user)         # {'이름': '김말똥', '전화번호': '01012341234', '주소': '123-123'}

def userInfo(name, phone, address):
    return {'이름': name, '전화번호':phone, '주소':address}

user = userInfo('김말똥', address='123-123', phone='01012341234')
print(type(user))   # <class 'dict'>
print(user)         # {'이름': '김말똥', '전화번호': '01012341234', '주소': '123-123'}

# 기본 매개변수값 지정
def userInfo(name='아무개', phone='번호없음ㅠㅠ', address='대체 어디사니?'):
    return {'이름': name, '전화번호':phone, '주소':address}

# 1. 인자 제공시
user = userInfo('김파이썬', '010-1234-1234', '123-123')
print(type(user))   # <class 'dict'>
print(user)         # {'이름': '김파이썬', '전화번호': '010-1234-1234', '주소': '123-123'}

# 2. 인자를 제공하지 않았을 때
user = userInfo()
print(type(user))   # <class 'dict'>
print(user)         # {'이름': '아무개', '전화번호': '번호없음ㅠㅠ', '주소': '대체 어디사니?'}

def stackFunc(arg, stack=[]):
    stack.append(arg)
    print(type(stack))
    print(stack)

stackFunc('월요일')
stackFunc('화요일')

# 일반적인 가변 인자 전달
def argsFunc(*args):
    print(type(args))
    print(args)

# 1. 아무것도 전달하지 않을 때
argsFunc()              # <class 'tuple'>, ()

# 2. 여러 인자를 전달 할 때
argsFunc(1,2,3,4,5)     # <class 'tuple'>, (1, 2, 3, 4, 5)

def favoriteMenu(loveMenu, likeMenu, *args):
    print(type(loveMenu))                   # <class 'str'>
    print('제일 좋아하는 메뉴는: ', loveMenu)    # 제일 좋아하는 메뉴는:  삼겹살
    print(type(likeMenu))                   # <class 'str'>
    print('좋아하는 메뉴는: ', likeMenu)       # 좋아하는 메뉴는:  갈
    print(type(args))                       # <class 'tuple'>
    print('욕심부리는 메뉴는: ', args)          # 욕심부리는 메뉴는:  ('치킨', '피자')

favoriteMenu('삼겹살', '갈비', '치킨', '피자')

# 가변 키워드 인자 전달
def kargsFunc(**kargs):
    print(type(kargs))      # <class 'dict'>
    print(kargs)            # {'a': '1', 'b': '2', 'c': '3'}

kargsFunc(a='1', b='2', c='3')

def mixFunc(*args, **kargs):
    print(type(args))   # <class 'tuple'>
    print(args)         # (1, 2, 3, 4)
    print(type(kargs))  # <class 'dict'>
    print(kargs)        # {'a': '1', 'b': '2', 'c': '3'}

mixFunc(1,2,3,4, a='1', b='2', c='3')
