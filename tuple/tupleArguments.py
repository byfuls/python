
def func(a, b, *tuple_c):
	ret = a + b
	for i in tuple_c:
		print(i)
	return ret

ret = func(1,2, (3,4))
