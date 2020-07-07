class PacketFormating:
    def __init__(self):
        self.__packet = bytearray(4)
        self.__offset = 0

    @property
    def packet(self):
        return self.__packet
    @property
    def totalLength(self):
        return None
    @totalLength.setter
    def totalLength(self, val):
        TLEN_LEN = 4
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
        SIZE_LEN = 4
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

        plen = len(self.__packet[4:])
        TLEN_LEN = 4
        convHex = plen.to_bytes(TLEN_LEN, 'big')
        self.__packet[0:4] = convHex
        self.__offset += TLEN_LEN

if __name__ == "__main__":
    t = PacketFormating()
    #t.totalLength = 321
    t.totalCount = 3
    t.index = 1
    t.size = 3
    t.pkdata = b'\x01\x02\x03'
    print(t.packet)
    print(len(t.packet))