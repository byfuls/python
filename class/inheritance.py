
class A:
	hello = {'1': 'a', '2': 'b'}
	def __init__(self):
		self.hi = {'a': 1, 'b': 2}

class B(A):
	def __init__(self):
		super().__init__()
		print(self.hi)
		#print(self.hello)

B()
