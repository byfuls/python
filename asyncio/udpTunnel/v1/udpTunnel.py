import asyncio
import threading
import janus
import time
import nest_asyncio
import socket
import select

'''
-> putter -> s_thread ->
<- getter <- r_thread <- 
'''

class udpTunnel(threading.Thread):
	def __init__(self, debug=False):
		super(udpTunnel,self).__init__()
		self.__loop = asyncio.get_event_loop()
		self.__debugging = debug
		nest_asyncio.apply(self.__loop)
		self.start()

	def __del__(self):
		self.__loop.close()

	def run(self):
		self.__loop.run_until_complete(self.launcher())

	async def t_close(self):
		if self.__debugging == True: print('[udpTunnel/t_close] start')
		self.__o_flag = False

		await self.__put_to_sender_que.async_q.put('drop')
		self.__o_sender.join()
		if self.__debugging == True: print('[udpTunnel/t_close] sender thread closed')
		self.__o_receiver.join()
		if self.__debugging == True: print('[udpTunnel/t_close] receiver thread closed')
		if self.__debugging == True: print('[udpTunnel/t_close] end')

	def t_start(self, ip, port):
		addr = (ip, port)
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.__o_flag = True
		self.__o_sender = threading.Thread(target=self.t_sender, args=(self.__put_to_sender_que,  addr))
		self.__o_receiver = threading.Thread(target=self.t_receiver, args=(self.__get_from_receiver_que, ))
		self.__o_sender.start()
		self.__o_receiver.start()

	async def launcher(self):
		self.__get_from_outer_que = asyncio.Queue()
		self.__put_to_sender_que = janus.Queue()
		self.__get_from_receiver_que = janus.Queue()

		put_to_sender_coro = self.a_put_to_sender(self.__get_from_outer_que, self.__put_to_sender_que)
		get_from_receiver_coro = self.a_get_from_receiver(self.__get_from_receiver_que)

		return await asyncio.gather(put_to_sender_coro, get_from_receiver_coro)

	async def a_put_to_sender(self, get_from_outer_que, put_to_sender_que):
		if self.__debugging == True: print('[put_to_sender] start')
		while True:
			if self.__debugging == True: print('[put_to_sender] ...')
			data = await get_from_outer_que.get()
			if self.__debugging == True: print(f'[put_to_sender] get from outer que, data: {data}')
			await put_to_sender_que.async_q.put(data)
			if self.__debugging == True: print(f'[put_to_sender] put to sender que, data: {data}')
		if self.__debugging == True: print('[put_to_sender] end')

	async def a_get_from_receiver(self, get_from_receiver_que):
		if self.__debugging == True: print('[get_from_receiver] start')
		while True:
			if self.__debugging == True: print('[get_from_receiver] ...')
			data = await get_from_receiver_que.async_q.get()
			if self.__debugging == True: print(f'[get_from_receiver] get data: {data}')
		if self.__debugging == True: print('[get_from_receiver] end')

	def t_sender(self, put_to_sender_que, addr):
		time.sleep(1)
		if self.__debugging == True: print('[sender] start')
		while self.__o_flag:
			if self.__debugging == True: print('[sender] ...')
			data = put_to_sender_que.sync_q.get()
			if self.__debugging == True: print('[sender] get') 
			if self.__debugging == True: print(f'[sender] get data: {data}')

			if 'drop' == data:
				self.__sock.close()
				break

			self.__sock.sendto(data.encode('utf-8'), addr)
		if self.__debugging == True: print('[sender] end')

	def t_receiver(self, get_from_receiver_que):
		time.sleep(1)
		if self.__debugging == True: print('[receiver] start')

		inputs = list()
		inputs.append(self.__sock)
		outputs = list()
		timeout = 1

		while self.__o_flag:
			if self.__debugging == True: print('[receiver] ...')
			readable, writable, exceptional = \
				select.select(inputs, outputs, inputs, timeout)
			for s in readable:
				if s == self.__sock:
					data, server = self.__sock.recvfrom(4096)
					if self.__debugging == True: print('[receiver] get') 
					if self.__debugging == True: print(f'[receiver] get data: {data}')
					get_from_receiver_que.sync_q.put(data)
			for s in exceptional:
				if self.__debugging == True: print('[receiver] socket err')
				break
		if self.__debugging == True: print('[receiver] end')

	async def input(self, data):
		if self.__debugging == True: print('[input] start')
		await self.__get_from_outer_que.put(data)
		if self.__debugging == True: print('[input] end')

if __name__ == '__main__':
	try:
		async def main_run(tunnel):
			try:
				print('[main_run] start')
				while True:
					print('[main_run] ...')
					await asyncio.sleep(2)
					await tunnel.input('hi')

					await asyncio.sleep(5)
					print('shutdown tunnel communicator - start')
					await tunnel.t_close()
					print('shutdown tunnel communicator - end')

					await asyncio.sleep(5)
					tunnel.t_start('127.0.0.1', 5001)
				print('[main_run] end')
			except asyncio.CancelledError:
				print('[main_run] cancelled')
				raise
			finally:
				print('[main_run] done')
			
		async def main():
			tunnel = udpTunnel(debug=True)
			tunnel.t_start('127.0.0.1', 5001)
			task = asyncio.create_task(main_run(tunnel))

			await task

		asyncio.run(main())
	except KeyboardInterrupt:
		print('done')
		exit(1)
