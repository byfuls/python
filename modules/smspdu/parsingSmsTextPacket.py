receivedSmsTextMessage = b'\r\n+CMT: "10001",,"20/10/23,10:04:56+36",128,0,0,0,"447785016005",145,15\r\nTest message123\r\n'

def parsingRecvSmsData(pkt):
	'''
	smsSender: 10001
	dontKnow0:
	sendDate: 20/10/23
	sendTime: 10:04:56+36
	dontKnow1: 128
	dontKnow2: 0
	dontKnow3: 0
	dontKnow4: 0
	dontKnow5: 447785016005
	dontKnow6: 145
	textLength: 15
	textMessage: Test message123
	'''
	_pkt = pkt
	pos = _pkt.find(b',')
	if pos == -1:
		print('not found')
		return
	idx = 0
	parsedSmsData = {}
	while pos != -1:
		sortedPkt = _pkt[:pos]
		print(f'[idx]:{idx}, [pos]:{pos}, [pkt]:{sortedPkt}')

		if idx == 0:	# sms sender
			s, e = sortedPkt.find(b'"'), sortedPkt.rfind(b'"')
			parsedSmsData['smsSender'] = sortedPkt[s+1:e]
		elif idx == 1:	# dont know
			parsedSmsData['dontKnow0'] = sortedPkt
		elif idx == 2:	# send date
			parsedSmsData['sendDate'] = sortedPkt[1:]
		elif idx == 3:	# send time
			parsedSmsData['sendTime'] = sortedPkt[:len(sortedPkt)-1]
		elif idx == 4:	# dont know
			parsedSmsData['dontKnow1'] = sortedPkt
		elif idx == 5:	# dont know
			parsedSmsData['dontKnow2'] = sortedPkt
		elif idx == 6:	# dont know
			parsedSmsData['dontKnow3'] = sortedPkt
		elif idx == 7:	# dont know
			parsedSmsData['dontKnow4'] = sortedPkt
		elif idx == 8:	# dont know
			parsedSmsData['dontKnow5'] = sortedPkt
		elif idx == 9:	# dont know
			parsedSmsData['dontKnow6'] = sortedPkt

		_pkt = _pkt[pos+1:]
		pos = _pkt.find(b',')
		idx+=1

	if pos == -1:	# sms text
		e = _pkt.find(b'\r\n')
		parsedSmsData['textLength'] = _pkt[:e]
		_pkt = _pkt[e+2:]
		e = _pkt.rfind(b'\r\n')
		parsedSmsData['textMessage'] = _pkt[:e]

	print(parsedSmsData)
	print(parsedSmsData['textMessage'])
		

if __name__ == "__main__":
	parsingRecvSmsData(receivedSmsTextMessage)
