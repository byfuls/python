import asyncio
import threading
import janus
import time
import sys

class makeInterval:
	def __init__(self, makeVal):
		super(makeInterval, self).__init__()
		self.__makeVal = (makeVal/1000000.0)
		self.__lastInputTime = time.time()
		self.__currTime = 0

	@property
	def interval_val(self):
		return self.__makeVal

	async def interval_check(self, putData):
		print('interval...')
		passData = putData

		self.__currTime = time.time()
		elapsed = self.__currTime - self.__lastInputTime
		print(f'makeVal: {self.__makeVal} // elapsed: {elapsed}')
		if self.__makeVal > elapsed:
			#time.sleep(self.__makeVal-elapsed)
			interv = self.__makeVal-elapsed
			await asyncio.sleep(interv)
			print(f'make interval !!!!!!!!!!!!!!! ({interv})')
		self.__lastInputTime = time.time()
		return passData

class asyncLoop(threading.Thread):
	def __init__(self):
		super(asyncLoop, self).__init__()
		self.__loop = asyncio.new_event_loop()
		self.__interval = makeInterval(2000)
		print(f'interval val: {self.__interval.interval_val}')

	def __enter__(self):
		print('enter')
		self.start()

	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit')
		return self

	def run(self):
		print('run')
		self.__loop.run_until_complete(self.asyncLauncher())

	async def asyncLauncher(self):
		print('asyncLauncher')
		coroutines = [self.looper(),]
		gather = await asyncio.gather(*coroutines, return_exceptions=True)
		return gather

	async def looper(self):
		self.queue = janus.Queue()
		print('looper ready')

		while True:
			get = await self.queue.async_q.get()
			print(f'loop..., val: {get}')
			# elapsed time check - start
			start_time = time.time()
			p = await self.__interval.interval_check('put data')
			elapsed_time = time.time() - start_time
			print(f'passed data: {p}')
			print('loop..., elapsed time: %0.05f' % elapsed_time)
			# elapsed time check - end

			# make delay options
			#await asyncio.sleep(1)

def run():
	loop = asyncLoop()
	loop.start()
	time.sleep(1)
	
	cnt = 0
	while True:
		print('main..., put')
		if cnt!=0 and (cnt % 10) == 0:
			time.sleep(5)
		else:
			loop.queue.sync_q.put(1)
		cnt = cnt + 1
		#time.sleep(1)


if __name__ == '__main__':
	try:
		run()
	except KeyboardInterrupt as msg:
		print('KeyboardInterrupt Done...')
		sys.exit(0)
