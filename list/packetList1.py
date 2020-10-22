
a = b'at+cmgs="10001"\r'
b = b'at+cmgs="10001"\r'

ret = a.find(b)
print(ret)
if ret:
	print('found')
else:
	print('not found')
