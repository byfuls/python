

class classObj:
	def __init__(self):
		print('__init__ called')
	def __del__(self):
		print('__del__ called')

cls = classObj()
del cls
