import asyncio

async def putter(queue):
	print('putter start')
	while True:
		print('putter ...')
		#val = input('input data: ')
		#print(f'input data: {val}')
		await queue.put('hi')
		await asyncio.sleep(3)
	print('putter end')

async def getter(queue):
	print('getter start')
	while True:
		print(f'getter...')
		data = await queue.get()
		print(f'getter, get data: {data}')
		#await asyncio.sleep(1)
	print('getter end')
		

loop = asyncio.get_event_loop()
queue = asyncio.Queue()
putter_coro = putter(queue)
getter_coro = getter(queue)

loop.run_until_complete(asyncio.gather(putter_coro, getter_coro))
loop.close()
