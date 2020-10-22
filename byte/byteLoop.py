import struct

bt = b'abcdef'

for b in bt:
	print(b)
	print(struct.pack('s', b.to_bytes(1, 'big')))
