import threading

class first():
	def __init__(self):
		print("first")

class second():
	def __init__(self):
		print("second")

class third(first, second, threading.Thread):
	def __init__(self):
		super(third, self).__init__()
		second.__init__(self)
		threading.Thread.__init__(self)
		print("third")

thr = third()
