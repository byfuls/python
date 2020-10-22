
ls = []

packet1 = b'packet-1'
packet2 = b'packet-2'
packet3 = b'packet-3'

print(ls)
ls.append(packet1)
print(ls)
ls.append(packet2)
print(ls)
ls.append(packet3)
print(ls)

print(len(ls))
for n in ls:
	print(f'packet list: {n}')

#ls.remove(packet1)
#print(ls)
#ls.remove(packet2)
#print(ls)


ls.pop(0)
print(ls)
