import time
import threading

class callThread():
	def __init__(self):
		self.__cycle = threading.Thread(target=self.__cycleThread, args=())

	def __cycleThread(self):
		while True:
			print('hihi')
			time.sleep(1)

	def begin(self):
		self.__cycle.start()

ct = callThread()
ct.begin()
print('hello')
