import asyncio
import threading

class asyncThread(threading.Thread):
	def __init__(self):
		super(asyncThread, self).__init__()
		self.__loop = asyncio.new_event_loop()

	def __enter__(self):
		self.start()

	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit')

	def run(self):
		self.__loop.run_until_complete(self.asyncLauncher())

	async def asyncLauncher(self):
		coroutines = [self.looper(),]
		gather = await asyncio.gather(*coroutines, return_exceptions=True)
		return gather

	async def looper(self):
		while True:
			await asyncio.sleep(1)
			print('looper ...')

with asyncThread() as asyncThr:
	print('gogogo')
