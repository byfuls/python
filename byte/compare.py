
a = b'\rAT-Command Interpreter ready\r\n'
print(a)


#ret = a[1:].find(b'AT-Command Interpreter ready')
ret = a[1:].find(b'AT-Command Interpreter ready\r\n')
print(ret)
print(len(a))
if ret >= 0:
	print('found')
else:
	print('not found')
