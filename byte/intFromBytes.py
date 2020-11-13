
packets = b'\x00\x01\x00\x02\x00\x03'
packetsLen = len(packets)
print(packetsLen)

getLength = packets[packetsLen-2:packetsLen]
v = int.from_bytes(getLength, byteorder='big')
print(v)
