
def sort_packet(in_packet):
	#--- sort in bytes
	# case 1, ERROR)
	#	(1) b'\x02\x0d\x0a\x45\x52\x52\x4f\x52\x0d'
	#	(2) b'\x0a\x03\xa0\xa4\x00\x00\x02
	search_head = b'\x02\x0d\x0a'
	search_tail = b'\x0d\x0a'
	ret = in_packet.find(search_head)
	if ret >= 0:
		head_point = ret
		ret = in_packet.rfind(search_tail)
		if ret >= 0:
			tail_point = ret
			sorted_packet = in_packet[head_point:tail_point+len(search_tail)]
			if head_point == 0:
				forward = True
				rested_packet = in_packet[tail_point+len(search_tail):]
			else:
				forward = False
				rested_packet = in_packet[:head_point]
			print(f'[sort] sorted packet: {sorted_packet}')
			print(f'[sort] rested packet: {rested_packet}')
		else:
			print(f'[sort] not found formatted packet')
	else:
		print(f'[sort] not found head')
		sorted_packet, rested_packet, forward = None, None, None
	return (in_packet, sorted_packet, rested_packet, forward)


def main():
	raw_error = b'\x02\x0d\x0a\x45\x52\x52\x4f\x52\x0d\x0a\x03\xa0\xa4\x00\x00\x02'	# contain 'ERROR'
	raw_ok = b'\x03\xa0\xa4\x00\x00\x02\x02\x0d\x0a\x4f\x4b\x0d\x0a' # contain 'OK'
	print(raw_error)
	print(raw_ok)

	#--- search in bytes
	search_key = 'OK'
	ret = raw_error.find(search_key.encode('utf-8'))
	if ret >= 0:
		print(f'[search] found key: {search_key}')
	else:
		print(f'[search] not found key: {search_key}')
	search_key = 'OK'
	ret = raw_ok.find(search_key.encode('utf-8'))
	if ret >= 0:
		print(f'[search] found key: {search_key}')
	else:
		print(f'[search] not found key: {search_key}')


	#--- sort
	raw_packet, sorted_packet, rested_packet, forward = sort_packet(b'\x01\x02\x03\x04\x05\x06\x07')
	if sorted_packet == None:
		print('[result packet] not found anything')

	raw_packet, sorted_packet, rested_packet, forward = sort_packet(raw_error)
	print(f'[result packet] raw packet: {raw_packet}')
	print(f'[result packet] sorted packet: {sorted_packet}')
	print(f'[result packet] rested packet: {rested_packet}')
	print(f'[result packet] direction forward: {forward}')

	raw_packet, sorted_packet, rested_packet, forward = sort_packet(raw_ok)
	print(f'[result packet] raw packet: {raw_packet}')
	print(f'[result packet] sorted packet: {sorted_packet}')
	print(f'[result packet] rested packet: {rested_packet}')
	print(f'[result packet] direction forward: {forward}')
	
if __name__ == "__main__":
	main()
