

def f_sum(a,b):
	if a > 10 or b > 10:
		raise Exception('hihi')
	else:
		return a+b

try:
	ret = f_sum(1,3)
	print(f'ret: {ret}')
except:
	print(f'except occur')

try:
	ret = f_sum(11,3)
	print(f'ret: {ret}')
except Exception as msg:
	print(f'except occur: {msg}')
