from collections import namedtuple

class data:
    def __init__(self, name):
        self.__name = name;
        self.__value1 = 1;
        self.__value2 = 2;
    @property
    def name(self):
        return self.__name
    @property
    def val1(self):
        return self.__value1
    @property
    def val2(self):
        return self.__value2

# prepare input data
a = data('a');
b = data('b');
c = data('c');
d = data('d');

# prepare namedtuple
titles = namedtuple('titles', 'a b c d')
# input class data to namedtuple
namedtuple_dict = titles(a,b,c,d)
# show input data
print(namedtuple_dict)

# get input data
print(f'a data: {namedtuple_dict.a}')
print(f'a data.name: {namedtuple_dict.a.name}')
print(f'a data.val1: {namedtuple_dict.a.val1}')
print(f'a data.val2: {namedtuple_dict.a.val2}')

print(f'b data: {namedtuple_dict.b}')
print(f'b data.name: {namedtuple_dict.b.name}')
print(f'b data.val1: {namedtuple_dict.b.val1}')
print(f'b data.val2: {namedtuple_dict.b.val2}')