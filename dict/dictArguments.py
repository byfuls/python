

### as-1
def func_as1(*args):
	print(args)
a = {'a': 1, 'b': 2, 'c': 3}
func_as1(a)


### as-2
def func_as2(**kargs):
	print(kargs)
func_as2(a_1=1, b_2=2, c_3=3)

### as-3
def func_as3(**kargs):
	print(kargs)
a = {'test1':1, 'test2':2, 'test3':3}
func_as3(**a)
