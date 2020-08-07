import asyncio
import threading
import janus
import time
import socket
from collections import namedtuple

class palletObj(threading.Thread):
	def __init__(self, cls, ip, port):
		super(palletObj, self).__init__()
		self.__loopPallet = asyncio.new_event_loop()
		#self.__loopPallet = asyncio.get_event_loop()
		self.__sender = None
		self.__receiver = None
		#self.__sq = janus.Queue()
		self.__sq = asyncio.Queue()
		self.__cls = cls
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__addr = (ip, port)
		self.start()
		print('palletobj, start')

	def __del__(self):
		self.__sock.close()
		self.__sq.close()

	def run(self):
		self.__loopPallet.run_until_complete(self.palletLauncher())
		print("palletobj, dead")

	async def palletLauncher(self):
		coroutines = [self.sender(self.__sq), self.receiver(self.__sq)]
		asyncGather = await asyncio.gather(*coroutines, return_exceptions=True)
		return asyncGather

	# udp socket
	def passto(self, msg):
		return self.__sock.sendto(msg, self.__addr)
	def getfrom(self):
		msg, server = self.__sock.recvfrom(4096)
		return msg 

	@property
	def sq(self):
		return self.__sq
	async def put_sq(self, t):
		print('pallet, put queue - start')
		await self.__sq.put(t)
		print('pallet, put queue - end')
	async def get_sq(self):
		print('pallet, get queue')
		return await self.__sq.get()

	#def init(self):
	#	__t_sender = asyncio.create_task(self.sender())		# todo: go to another thread
	#	__t_receiver = asyncio.create_task(self.receiver())	# todo: go to another thread
	#	self.__sender = __t_sender
	#	self.__receiver = __t_receiver

	#async def wait_done(self):
	#	done_sender, pending_sender = await asyncio.wait({self.__sender})
	#	done_receiver, pending_receiver = await asyncio.wait({self.__receiver})
	#	if self.__sender in done_sender:
	#		print("pallet, SENDER DONE")
	#	if self.__receiver in done_receiver:
	#		print("pallet, RECEIVER DONE")
	#	return

	def done(self):
		self.__sender.cancel()
		self.__receiver.cancel()

	async def sender(self, queue):
		while True:
			print('sender, ready ...')
			#msg = await self.__sq.async_q.get()
			#msg = await queue.get()
			#print(f'sender, get msg: {msg}')
			#self.passto(msg)
			await asyncio.sleep(1)

	async def receiver(self, queue):
		while True:
			print('receiver, ready ...')
			#msg = self.getfrom()
			#print(f'receiver, get msg: {msg}')
			await asyncio.sleep(1)

class voiceTransaction(threading.Thread):
	def __init__(self, cls):
		super(voiceTransaction, self).__init__()
		self.__loopTunnel = asyncio.new_event_loop()
		self.__cls = cls
		self.start()

	def run(self):
		self.__vt = self.voiceTransaction()

	def voiceTransaction(self):
		self.__loopTunnel.run_until_complete(self.tunnelLauncher())

	def putTunnel(self, msg):
		self.__putTunnelQueue.sync_q.put(msg)
		print(f'tunnel, put msg: {msg}')

	async def tunnelLauncher(self):
		coroutines = [self.tunnel(), self.pallet()]
		asyncGather = await asyncio.gather(*coroutines, return_exceptions=True)
		return asyncGather

	async def pallet(self):
		self.__putPalletQueue = janus.Queue()

		while True:
			print('pallet, start')
			msg = await self.__putPalletQueue.async_q.get()
			if msg == 'RUN':
				print('pallet, RUN - init')
				#self.__palletInfo.init()
				#await self.__palletInfo.wait_done()
			print('pallet, done')


	async def tunnel(self):
		print('tunnel, launch...')
		self.__putTunnelQueue = janus.Queue()

		_state = False
		while True:
			print('tunnel, ready...')
			msg = await self.__putTunnelQueue.async_q.get()
			print('tunnel, get msg')
			print(f'tunnel, state: {_state} && msg: {msg}')
			if _state is False and msg == 'RUN':
				print(f'tunnel, start')
				self.__palletInfo = palletObj(self.__cls, 'localhost', 5001); _state = True
				#self.__putPalletQueue.sync_q.put(msg)
				print(f"tunnel, put 'RUN' msg")
				self.__putPalletQueue.sync_q.put('RUN')
			elif _state is True and msg == 'FIN':
				print(f'tunnel, finish')
				self.__palletInfo.done()
				del self.__palletInfo; _state = False
			else:
				print(f'tunnel, bypass')
				await self.__palletInfo.put_sq(msg)
			print('tunnel, again~~~')

class tmp:
	def __init__(self):
		self.a = 3
	@property
	def bypass(self):
		return self.a

if __name__ == '__main__':
	import socket

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('localhost', 5000))

	t = tmp()
	vt = voiceTransaction(t)
	while True:
		msg, address = sock.recvfrom(4096)
		msg = msg.decode('utf-8')
		print('main, received %s bytes from %s' % (len(msg), address))
		print('main, msg: %s' % msg)

		vt.putTunnel(msg)
		time.sleep(3)
		vt.putTunnel('123')
