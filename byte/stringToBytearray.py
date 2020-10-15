
packet = bytearray()

header = "ABCD"
dit = "|"
serialId = "1302"

packet += header.encode('utf-8')
packet += dit.encode('utf-8')
packet += serialId.encode('utf-8')

print(packet)
