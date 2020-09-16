
str = 'post/2020/09/pork_20200915_1.jpg'

ret = str.find('/')
print(ret)
print(str[ret+1:])

ret = str.rfind('/')
print(ret)
print(str[ret+1:])
