

class serial_recv:
	def __init__(self, ):
		self.__dir_sz = 1
		self.__min_sz = 2+self.__dir_sz
		self.__dir_dict = {
							#b'\x00': 'NONE',
							b'\x01': 'MAIN',
							b'\x02': 'GTM',
							b'\x03': 'SIM',
							b'\x04': 'CMX',
							b'\x05': 'MP_WORKER',
							b'\x06': 'SIM_WORKER',
							b'\x07': 'VOICE_WORKER',
							b'\x08': 'SERIAL_WORKER' }
		self.__packet = bytearray(128)
		self.__state = False

	def append(self, packet):
		print(f'[append] input: {packet} // {len(packet)}')

		if len(packet) == 1:
			if packet not in self.__dir_dict:
				print(f'[append] unknown signal received: {packet}')
				self.__state = False
				self.__packet.clear()
				return False
			elif self.__state == True:
				bef_pkt = self.__packet[:]
				self.__packet.clear()
				self.__packet[0:] = packet
				print(f'[append] change: {self.__packet}')
				return bef_pkt
			else:
				self.__state = True
				self.__packet.clear()
				self.__packet[0:] = packet
				print(f'[append] new: {self.__packet}')
				return True
		#elif len(packet) == 2:
		#	print(f'[append] noise')
		#	return False
		elif len(packet) >= 2 and self.__state == True:
			self.__packet += packet
			self.__state = False
			print(f'[append] data: {self.__packet}')
			return self.__packet
		else:
			print(f'[append] unknown long packet received: {packet}')
			self.__state = False
			self.__packet.clear()
			return False
			

if __name__ == '__main__':
	gsm = serial_recv()

	ret = gsm.append(b'\x03')
	print(f'[main] {ret}')
	#if type(ret).__name__ != 'bytearray':
	#	print('[main] again')

	ret = gsm.append(b'\xa0\xa4\x00\x00\x02')
	print(f'[main] {ret}')

	ret = gsm.append(b'\x03')
	print(f'[main] {ret}')

	ret = gsm.append(b'\x7f\x04')
	print(f'[main] {ret}')

	#print(type(ret))
	#print(type(ret).__name__)
	#if type(ret).__name__ != 'bytearray':
	#	print('[main] again')

	#print(f'[main] remain:{gsm.packet}')
