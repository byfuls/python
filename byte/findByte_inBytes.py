
buf = b'\x01\x02\x03\xa0'

pos = buf.find(b'\xd0')
print(f'pos: {pos} len: {len(buf)}')
