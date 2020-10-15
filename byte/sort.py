import struct

####################################################
#		  0   1   2   3   4   5   6
raw = b'\x01\x02\x03\x04\x05\x06\x07'
lgth = len(raw)
print(raw)
print(raw[0:lgth])
print(raw[3:1:-1])


####################################################
packet = struct.pack('1b 20s', 2, "CONID|64002|64000|||".encode('utf-8'))
print(packet)
print(packet[0])
print(packet[1])
print(packet[2])

foundList = []
foundDict = {}
foundI = 0
while True:
	idx = packet.find('|'.encode('utf-8'))
	if 0 > idx:
		break
	print(f'found: {idx}')
	print(f'packet: {packet}')

	foundList.append(packet[0:idx])
	foundDict[foundI] = packet[0:idx]
	foundI+=1

	packet = packet[idx+1:]

print(foundList)
print(foundDict)
