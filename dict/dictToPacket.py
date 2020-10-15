

dit = '|'
obj = {
    'command': "CS01",
    'id': 'id',
    'mcc': 'mcc',
    'mnc': 'mnc',
    'lac': 'lac',
    'arfcn': 'arfcn',
    'mm_state': 'mm_state',
    'state': 'state',
    'sub_state': 'sub_state',
    'dbm': 'dbm',
    'cell_id': 'cell_id',
    'bsic': 'bsic'
}

pkt = bytearray()
for o in obj:
	print(o)
	pkt += obj[o].encode('utf-8')
	pkt += dit.encode('utf-8')

print(pkt)
