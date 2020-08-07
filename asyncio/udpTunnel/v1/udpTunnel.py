import asyncio
import threading
import janus
import time
import nest_asyncio
import socket

'''
-> putter -> s_thread ->
<- getter <- r_thread <- 
'''

class udpTunnel(threading.Thread):
	def __init__(self):
		super(udpTunnel,self).__init__()
		self.__loop = asyncio.get_event_loop()
		nest_asyncio.apply(self.__loop)
		self.start()

	def __del__(self):
		self.__loop.close()

	def run(self):
		self.__loop.run_until_complete(self.launcher())

	def t_close(self):
		self.__o_sender.stop()
		self.__o_receiver.stop()

	def t_start(self, ip, port):
		addr = (ip, port)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.__o_sender = threading.Thread(target=self.t_sender, args=(self.__put_to_sender_que, sock, addr))
		self.__o_receiver = threading.Thread(target=self.t_receiver, args=(self.__get_from_receiver_que, sock))
		self.__o_sender.start()
		self.__o_receiver.start()

	async def launcher(self):
		self.__get_from_outer_que = asyncio.Queue()
		self.__put_to_sender_que = janus.Queue()
		self.__get_from_receiver_que = janus.Queue()

		put_to_sender_coro = self.a_put_to_sender(self.__get_from_outer_que, self.__put_to_sender_que)
		get_from_receiver_coro = self.a_get_from_receiver(self.__get_from_receiver_que)

		#self.__o_sender = threading.Thread(target=self.t_sender, args=(self.__put_to_sender_que,))
		#self.__o_receiver = threading.Thread(target=self.t_receiver, args=(self.__get_from_receiver_que,))
		#self.__o_sender.start()
		#self.__o_receiver.start()

		return await asyncio.gather(put_to_sender_coro, get_from_receiver_coro)

	async def a_put_to_sender(self, get_from_outer_que, put_to_sender_que):
		print('[put_to_sender] start')
		while True:
			print('[put_to_sender] ...')
			data = await get_from_outer_que.get()
			print(f'[put_to_sender] get from outer que, data: {data}')
			await put_to_sender_que.async_q.put(data)
			print(f'[put_to_sender] put to sender que, data: {data}')
		print('[put_to_sender] end')

	async def a_get_from_receiver(self, get_from_receiver_que):
		print('[get_from_receiver] start')
		while True:
			print('[get_from_receiver] ...')
			data = await get_from_receiver_que.async_q.get()
			print(f'[get_from_receiver] get data: {data}')
		print('[get_from_receiver] end')

	def t_sender(self, put_to_sender_que, sock, addr):
		print('[sender] start')
		while True:
			print('[sender] ...')
			data = put_to_sender_que.sync_q.get()
			print(f'[sender] get data: {data}')

			sock.sendto(data.encode('utf-8'), addr)
		print('[sender] end')

	def t_receiver(self, get_from_receiver_que, sock):
		print('[receiver] start')
		while True:
			print('[receiver] ...')
			data, server = sock.recvfrom(4096)
			print(f'[receiver] get data: {data}')
			get_from_receiver_que.sync_q.put(data)
		print('[receiver] end')

	async def input(self, data):
		print('[input] start')
		await self.__get_from_outer_que.put(data)
		print('[input] end')

if __name__ == '__main__':
	try:
		async def main_run(tunnel):
			try:
				print('[main_run] start')
				while True:
					await asyncio.sleep(1)
					await tunnel.input('hi')
				print('[main_run] end')
			except asyncio.CancelledError:
				print('[main_run] cancelled')
				raise
			finally:
				print('[main_run] done')
			
		async def main():
			tunnel = udpTunnel()
			tunnel.t_start('127.0.0.1', 5001)
			task = asyncio.create_task(main_run(tunnel))

			#await asyncio.sleep(1)
			#task.cancel()

			await task

		asyncio.run(main())
	except KeyboardInterrupt:
		print('done')
		exit(1)
