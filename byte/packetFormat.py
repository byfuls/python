class PacketFormating:
	DEFAULT_HEADER_SIZE = 4

	def __init__(self, headerSize=DEFAULT_HEADER_SIZE):
		self.__headerSize = headerSize;
		self.__packet = bytearray(self.__headerSize)
		self.__offset = 0

	@property
	def packet(self):
		return self.__packet
	@property
	def len(self):
		return self.__offset

	def clear(self):
		self.__packet = bytearray(self.__headerSize)
		self.__offset = 0

	@property
	def totalLength(self):
		return None
	@totalLength.setter
	def totalLength(self, val):
		TLEN_LEN = self.__headerSize
		convHex = val.to_bytes(TLEN_LEN, 'big')
		self.__packet[0:] = convHex
		self.__offset += TLEN_LEN
	@property
	def totalCount(self):
		return None
	@totalCount.setter
	def totalCount(self, val):
		TCNT_LEN = 2
		convHex = val.to_bytes(TCNT_LEN, 'big')
		self.__packet += convHex
		self.__offset += TCNT_LEN
	@property
	def index(self):
		return None
	@index.setter
	def index(self, val):
		INDEX_LEN = 2
		convHex = val.to_bytes(INDEX_LEN, 'big')
		self.__packet += convHex
		self.__offset += INDEX_LEN
	@property
	def size(self):
		return None
	@size.setter
	def size(self, val):
		SIZE_LEN = self.__headerSize
		convHex = val.to_bytes(SIZE_LEN, 'big')
		self.__packet += convHex
		self.__offset += SIZE_LEN
	@property
	def pkdata(self):
		return None
	@pkdata.setter
	def pkdata(self, val):
		self.__packet += val
		self.__offset += len(val)

		plen = len(self.__packet[self.__headerSize:])
		TLEN_LEN = self.__headerSize
		if TLEN_LEN != 0:
			convHex = plen.to_bytes(TLEN_LEN, 'big')
			self.__packet[0:self.__headerSize] = convHex
			self.__offset += TLEN_LEN

if __name__ == "__main__":
	#t = PacketFormating()
	##t.totalLength = 321
	#t.totalCount = 3
	#t.index = 1
	#t.size = 3
	#t.pkdata = b'\x01\x02\x03'
	#print(t.packet)
	#print(len(t.packet))

	t = PacketFormating(0)
	print(t.packet)
	t.pkdata = b'\x01\x02\x03'
	print(t.packet)
	print(t.len)
	t.pkdata = b'\x04\x05\x06'
	print(t.packet)
	print(t.len)

	t.clear()
	print(t.packet)
	print(t.len)
	t.pkdata = b'\x01\x02\x03'
	print(t.packet)
	print(t.len)
	t.pkdata = b'\x04\x05\x06'
	print(t.packet)
	print(t.len)
