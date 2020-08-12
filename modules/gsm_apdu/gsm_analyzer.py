

class gsm_analyze:
	def __init__(self):
		self.__header_length = 5

		self.__select = b'\xa0\xa4'
		self.__read_binary = b'\xa0\xb0'
		self.__update_binary = b'\xa0\xd6'
		self.__read_record = b'\xa0\xb2'
		self.__update_record = b'\xa0\xdc'
		self.__verify_chv = b'\xa0\x20'
		self.__change_chv = b'\xa0\x24'
		self.__unblock_chv = b'\xa0\x2c'
		self.__run_gsm_algorithm = b'\xa0\x88'
		self.__get_response = b'\xa0\xc0'
		self.__get_status = b'\xa0\xf2'
		self.__packet = bytearray(0)

	def append(self, packet):
		print(f'[append] input: {packet}')

		self.__packet += packet
		print(f'[append] full: {self.__packet}')

		pos = self.__packet.find(self.__select)
		if pos >= 0:
			ret = self.__analyze_select(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__read_binary)
		if pos >= 0:
			ret = self.__analyze_read_binary(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__update_binary)
		if pos >= 0:
			ret = self.__analyze_update_binary(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__read_record)
		if pos >= 0:
			ret = self.__analyze_read_record(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__update_record)
		if pos >= 0:
			ret = self.__analyze_update_record(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__verify_chv)
		if pos >= 0:
			print("NOT SUPPORTED NOW 'VERIFY CHV'")
			return False

		pos = self.__packet.find(self.__change_chv)
		if pos >= 0:
			print("NOT SUPPORTED NOW 'CHANGE CHV'")
			return False

		pos = self.__packet.find(self.__unblock_chv)
		if pos >= 0:
			print("NOT SUPPORTED NOW 'UNBLOCK CHV'")
			return False

		pos = self.__packet.find(self.__run_gsm_algorithm)
		if pos >= 0:
			print("NOT SUPPORTED NOW 'RUN GSM ALGORITHM'")
			return False

		pos = self.__packet.find(self.__get_response)
		if pos >= 0:
			ret = self.__analyze_get_response(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.find(self.__get_status)
		if pos >= 0:
			ret = self.__analyze_get_status(self.__packet[pos:])
			if ret > 0:
				tmp = self.__packet[:pos+ret]
				self.__packet = self.__packet[pos+ret:]
				return tmp
			else:
				return ret

		pos = self.__packet.rfind(b'\x0a')
		if 0x02 == self.__packet[0] and pos >= 0:
			tmp = self.__packet[:pos]
			self.__packet.clear()
			#self.__packet = self.__packet[pos:]
			return tmp

		pos = self.__packet.rfind(b'\x0d')
		if 0x02 == self.__packet[0] and pos >= 0:
			tmp = self.__packet[:pos]
			self.__packet.clear()
			return tmp

		if 0x03 == self.__packet[0] and 2 >= len(self.__packet) and 1 != len(self.__packet):

			print(f'[append] remain: {self.__packet}')
			print(f'[append] clear')
			self.__packet.clear()
			return -7

		if 0x00 == self.__packet[0]:
			print(f'[append] remain: {self.__packet}')
			print(f'[append] clear')
			self.__packet.clear()
			return -8

		print(f'[append] remain: {self.__packet}')
		return -9

	@property
	def packet(self):
		return self.__packet

	def __clear(self):
		print(f'[clear] done')
		self.__select_flag = False
		self.__read_binary_flag = False
		self.__update_binary_flag = False
		self.__read_record_flag = False
		self.__update_record_flag = False
		self.__verify_chv__flag = False
		self.__change_chv__flag = False
		self.__unblock_chv_flag = False
		self.__run_gsm_algorithm_flag = False
		self.__get_response_flag = False
		self.__get_status_flag = False
		self.__packet = bytearray(0)

	def __analyze_get_status(self, packet):
		print(f'[get_status] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xf2' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_get_response(self, packet):
		print(f'[get_response] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xc0' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_update_record(self, packet):
		print(f'[update_record] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xdc' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_read_record(self, packet):
		print(f'[read_record] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xb2' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_update_binary(self, packet):
		print(f'[update_binary] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xd6' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_read_binary(self, packet):
		print(f'[read_binary] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		if b'\xa0\xb0' != packet[pos:pos+2]:
			return -2
		pos= pos+2+2;
		lgth = packet[pos]

		if self.__header_legnth+lgth > tlen:
			return -3
		else:
			return self.__header_length_lgth

	def __analyze_select(self, packet):
		print(f'[select] {packet} / {len(packet)}')
		pos = 0
		tlen = len(packet)
		if self.__header_length >= tlen: return -1

		print(f'[select] {packet[pos:pos+2]}')
		if b'\xa0\xa4' != packet[pos:pos+2]:
			return -2;
		pos= pos+2+2;
		lgth = packet[pos]

		print(f'[select] {self.__header_length+lgth}:{tlen}')
		if self.__header_length+lgth > tlen:
			return -3
		else:
			return self.__header_length+lgth


if __name__ == '__main__':
	gsm = gsm_analyze()

	ret = gsm.append(b'\x03\xa0\xa4\x01\x02\x02')
	print(f'[main] {ret}')
	if type(ret).__name__ != 'bytearray':
		print('[main] again')

	ret = gsm.append(b'\x01\x02\x01\x02')
	print(f'[main] {ret}')
	print(type(ret))
	print(type(ret).__name__)
	if type(ret).__name__ != 'bytearray':
		print('[main] again')

	print(f'[main] remain:{gsm.packet}')
