from optparse import OptionParser
import socket
import pickle
import sys

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 10000

class controller:
	USAGE =	'''usage: %prog [options] arg
	-a, --address : connect server by address info
	-l, --list : show process list all
	-p, --print : show process print all
	-s, --show [serial no.] : show one
	-o, --on [serial no.] : power on process
	-f, --off [serial no.] : power off process
	-u, --up [serial no.] : launch process
	-d, --down [serial no.] : kill process
	-w, --watch [serial no.] : watch gateway(=serial) '''	
	SIZE = 102400

	def __init__(self, DEBUG=False):
		self.__parser = OptionParser(controller.USAGE)
		self.__debug = DEBUG
		self.__parser.add_option("-a", "--address", dest="address", action="store_true")
		self.__parser.add_option("-l", "--list", dest="list", action="store_true")
		self.__parser.add_option("-p", "--print", dest="print", action="store_true")
		self.__parser.add_option("-s", "--show", dest="show", action="store_true")
		self.__parser.add_option("-o", "--on", dest="on", action="store_true")
		self.__parser.add_option("-f", "--off", dest="off", action="store_true")
		self.__parser.add_option("-u", "--up", dest="up", action="store_true")
		self.__parser.add_option("-d", "--down", dest="down", action="store_true")
		self.__parser.add_option("-w", "--watch", dest="watch", action="store_true")

		self.__address = None
		self.__list = None
		self.__print = None
		self.__show = None
		self.__on = None
		self.__off = None
		self.__up = None
		self.__down = None
		self.__watch = None

	def __enter__(self):
		(options, args) = self.__parser.parse_args()
		if self.__debug:
			print(f'[parser-return] options:{options} args:{args}')
			print(f'[parser-return] options type:{type(options)}')
		if not (options.address or options.list or options.print or options.show or options.on or options.off or options.up or options.down or options.watch):
			self.__parser.error('incorrect number of arguments')
			self.__exit__()
		
		if options.address:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			h, p = tuple(args.pop(0).split(':'))
			if self.__debug: print(f'[options-sorting] list true')
			self.__address = (h, int(p))
		if options.list:
			if self.__debug: print(f'[options-sorting] list true')
			self.__list = True
		if options.print:
			if self.__debug: print(f'[options-sorting] list true')
			self.__print = True
		if options.show:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			t = args.pop(0)
			if self.__debug: print(f'[options-sorting] on true, arg:{t}:{type(t)}')
			self.__show = t
		if options.on:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			t = args.pop(0)
			if self.__debug: print(f'[options-sorting] on true, arg:{t}:{type(t)}')
			self.__on= t
		if options.off:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			t = args.pop(0)
			if self.__debug: print(f'[options-sorting] off true, arg:{t}:{type(t)}')
			self.__off = t
		if options.up:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			t = args.pop(0)
			if self.__debug: print(f'[options-sorting] up true, arg:{t}:{type(t)}')
			self.__up = t
		if options.down:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			if self.__debug: print(f'[options-sorting] down true')
			t = args.pop(0)
			self.__down = t
		if options.watch:
			if not len(args):
				self.__parser.error('incorrect number of arguments')
				self.__exit__()
			if self.__debug: print(f'[options-sorting] watch true')
			t = args.pop(0)
			self.__watch = t

		if self.__address is None:
			self.__serverAddr = (DEFAULT_HOST, DEFAULT_PORT)
		else:
			self.__serverAddr = self.__address

		print(f'[connect] server address: {self.__serverAddr}')
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__socket.connect(self.__serverAddr)
		return self
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.__socket.close()
		exit(0)

	@property
	def debug(self): return self.__debug
	@property
	def address(self): return self.__address
	@property
	def list(self): return self.__list
	@property
	def print(self): return self.__print
	@property
	def show(self): return self.__show
	@property
	def on(self): return self.__on
	@property
	def off(self): return self.__off
	@property
	def up(self): return self.__up
	@property
	def down(self): return self.__down
	@property
	def watch(self): return self.__watch

	def listAll(self):
		buf = bytes()
		buf += 'l'.encode()
		if self.__debug: print(f'send msg: {buf}')
		self.__socket.send(buf)
		rcv = self.__socket.recv(controller.SIZE)
		if self.__debug: print(f'recv msg: {rcv}')
		pkl_data = pickle.loads(rcv)
		if self.__debug: print(f'pkl data: {pkl_data}')

		print(f'[DEBUG] count:{len(pkl_data)}')

		for gwobj in pkl_data:
			print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
			print('%-15s : %.04s' %("serial no", gwobj['serial-no']))
			print('%-15s : %.10s' %("unique id", gwobj['unique-id']))
			print('%-15s : %.150s' %("virt_command", gwobj['virt_command']))
			print('%-15s : %.24s' %("virt_pid", gwobj['virt_pid']))
			print('%-15s : %.24s' %("virt_uptime", gwobj['virt_uptime']))
			print('%-15s : %.24s' %("virt_upcount", gwobj['virt_upcount']))
			print('%-15s : %.150s' %("gw_command", gwobj['gw_command']))
			print('%-15s : %.24s' %("gw_pid", gwobj['gw_pid']))
			print('%-15s : %.24s' %("gw_uptime", gwobj['gw_uptime']))
			print('%-15s : %.24s' %("gw_upcount", gwobj['gw_upcount']))
			print('%-15s : %.20s' %("vender-id", gwobj['vender-id']))
			print('%-15s : %.20s' %("product-id", gwobj['product-id']))
			print('%-15s : %.20s' %("state", gwobj['switch']))
			print('%-15s : %.20s' %("online", gwobj['online']))
			print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')

	def printAll(self):
		buf = bytes()
		buf += 'l'.encode()
		if self.__debug: print(f'send msg: {buf}')
		self.__socket.send(buf)
		rcv = self.__socket.recv(controller.SIZE)
		if self.__debug: print(f'recv msg: {rcv}')
		pkl_data = pickle.loads(rcv)
		if self.__debug: print(f'pkl data: {pkl_data}')

		if self.__debug: print(f'[DEBUG] count:{len(pkl_data)}')

		print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
		# unique serial state online virt-pid virt-uptime virt-upcount gw-pid gw-uptime gw-upcount vender-id product-id
		print('%-10s %-6s %-5s %-6s %-10s %-18s %-11s %-10s %-18s %-11s %-10s %-10s'
			% ('id', 'serial', 'state', 'online', 'virt-pid', 'virt-time', 'virt-count', 'gw-pid', 'gw-time', 'gw-count', 'vender', 'product'))
		print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
		for gwobj in pkl_data:
			print('%-10s %-6s %-5s %-6s %-10s %-18s %-11s %-10s %-18s %-11s %-10s %-10s'
				% (gwobj['unique-id'], gwobj['serial-no'], gwobj['switch'], gwobj['online']
					, gwobj['virt_pid'], gwobj['virt_uptime'], gwobj['virt_upcount'], gwobj['gw_pid'], gwobj['gw_uptime'], gwobj['gw_upcount']
					, gwobj['vender-id'], gwobj['product-id']))
		print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')

	def showOne(self, serial):
		if self.__debug: print(f'[showOne] serial:{serial}')
		buf = bytes()
		buf += 's'.encode()
		buf += serial.encode()
		if self.__debug: print(f'send msg: {buf}')
		self.__socket.send(buf)
		rcv = self.__socket.recv(controller.SIZE)
		if self.__debug: print(f'recv msg: {rcv}')
		pkl_data = pickle.loads(rcv)
		if self.__debug: print(f'pkl data: {pkl_data}')

		for gwobj in pkl_data:
			print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
			print('%-15s : %.04s' %("serial no", gwobj['serial-no']))
			print('%-15s : %.10s' %("unique id", gwobj['unique-id']))
			print('%-15s : %.150s' %("virt_command", gwobj['virt_command']))
			print('%-15s : %.24s' %("virt_pid", gwobj['virt_pid']))
			print('%-15s : %.24s' %("virt_uptime", gwobj['virt_uptime']))
			print('%-15s : %.24s' %("virt_upcount", gwobj['virt_upcount']))
			print('%-15s : %.150s' %("gw_command", gwobj['gw_command']))
			print('%-15s : %.24s' %("gw_pid", gwobj['gw_pid']))
			print('%-15s : %.24s' %("gw_uptime", gwobj['gw_uptime']))
			print('%-15s : %.24s' %("gw_upcount", gwobj['gw_upcount']))
			print('%-15s : %.20s' %("vender-id", gwobj['vender-id']))
			print('%-15s : %.20s' %("product-id", gwobj['product-id']))
			print('%-15s : %.20s' %("state", gwobj['switch']))
			print('%-15s : %.20s' %("online", gwobj['online']))
			print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')

	def switch(self, serial, onoff):
		if self.__debug: print(f'[switch] serial:{serial} onoff:{onoff}')
		buf = bytes()
		buf += 'o'.encode() if onoff == True else 'f'.encode()
		buf += serial.encode()
		if self.__debug: print(f'send msg: {buf}')
		self.__socket.send(buf)
		rcv = self.__socket.recv(controller.SIZE)
		if self.__debug: print(f'recv msg: {rcv}')

	def online(self, serial, onoff):
		if self.__debug: print(f'[online] serial:{serial} onoff:{onoff}')
		buf = bytes()
		buf += 'u'.encode() if onoff == True else 'd'.encode()
		buf += serial.encode()
		if self.__debug: print(f'send msg: {buf}')
		self.__socket.send(buf)
		rcv = self.__socket.recv(controller.SIZE)
		if self.__debug: print(f'recv msg: {rcv}')

if __name__ == "__main__":
	#test = controller(HOST, PORT, True)
	#test.printAll()
	#exit(0)

	with controller(False) as ctl:
		if ctl.address:
			if ctl.debug: print('[main] address up')
			# todo 
		if ctl.list:
			if ctl.debug: print('[main] list up')
			ctl.listAll()
		if ctl.print:
			if ctl.debug: print('[main] print up')
			ctl.printAll()
		if ctl.show:
			if ctl.debug: print('[main] show up')
			ctl.showOne(ctl.show)
		if ctl.on:
			if ctl.debug: print('[main] on up')
			ctl.switch(ctl.on, True)
		if ctl.off:
			if ctl.debug: print('[main] off up')
			ctl.switch(ctl.off, False)
		if ctl.up:
			if ctl.debug: print('[main] up up')
			ctl.online(ctl.up, True)
		if ctl.down:
			if ctl.debug: print('[main] down up')
			ctl.online(ctl.down, False)
		if ctl.watch:
			if ctl.debug: print('[main] watch up')
