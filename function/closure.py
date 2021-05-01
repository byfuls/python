
def menuListClosure():
    menu = []
    def list(name):
        menu.append(name)
        return menu
    return list

menuList = menuListClosure()
print(type(menuList))       # <class 'function'>
print(menuList)             # <function menuListCloser.<locals>.list at 0x1096d8820>

print(menuList('치킨'))       # ['치킨']
print(menuList('피자'))       # ['치킨', '피자']
print(menuList('삼겹살'))      # ['치킨', '피자', '삼겹살']
print(menuList('갈비'))       # ['치킨', '피자', '삼겹살', '갈비']

print(menuList.__code__.co_varnames)        # 지역변수 : ('name',)
print(menuList.__code__.co_freevars)        # 자유변수 : ('menu',)

print(menuList.__closure__)         # (<cell at 0x106c58fd0: list object at 0x106b05540>,)
print(menuList.__closure__[0].cell_contents)    # ['치킨', '피자', '삼겹살', '갈비']