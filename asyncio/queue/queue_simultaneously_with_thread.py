import asyncio
import threading
import janus
import time

'''
-> putter -> s_thread ->
<- getter <- r_thread <- 
'''


async def putter(p_queue, queue, t_queue):
	print('putter start')
	print(p_queue)
	while True:
		print('putter ...')

		data = await queue.get()
		#data = await p_queue.async_q.get()
		await t_queue.async_q.put(data)
	print('putter end')

async def getter(queue, t_queue):
	print('getter start')
	while True:
		#print(f'getter...')
		#data = await queue.get()
		#print(f'getter, get data: {data}')
		await asyncio.sleep(1)
	print('getter end')
		


def s_thread(t_queue):
	while True:
		#pass
		print('s_thread ...')
		data = t_queue.sync_q.get()
		print(f's_thread, get data: {data}')
		#data = t_queue.get()

def r_thread(t_queue):
	while True:
		#print('r_thread ...')
		time.sleep(1)
		#t_queue.put('hello')

async def launcher(p_queue):
	queue = asyncio.Queue()
	t_queue = janus.Queue()
	
	putter_coro = putter(p_queue, queue, t_queue)
	getter_coro = getter(queue, t_queue)

	s = threading.Thread(target=s_thread, args=(t_queue,))
	s.start()
	r = threading.Thread(target=r_thread, args=(t_queue,))
	r.start()

	return await asyncio.gather(putter_coro, getter_coro)

# input, src thread
def p_src(p_queue):
	print('p_src start')
	while True:
		print(f'p_src ...')
		val = input('input value: ')
		print(f'input data: {val}')
		p_queue.sync_q.put(val)

async def src_launcher():
	print('2')
	p_queue = janus.Queue()
	p = threading.Thread(target=p_src, args=(p_queue,))
	p.start()
	return p_queue

print('1')
p_q = src_launcher()

# coroutine 
loop = asyncio.get_event_loop()
loop.run_until_complete(launcher(p_q))
loop.close()
