
def tmpFunc():
	packet = "TEST MESSAGE".encode('utf-8')
	return (True, packet)

def tmpCall():
	return tmpFunc()

a, b = tmpCall()

print(a)
print(b)
