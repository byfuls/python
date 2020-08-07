import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5000)

while True:
	try:
		message = input('input message: ')
		print(message)
	
		# Send data
		print("sending '%s'" % message)
		sent = sock.sendto(bytes(message, 'utf-8'), server_address)
	
		# Receive response
		print('waiting to receive')
		data, server = sock.recvfrom(4096)
		print("received '%s'" % data)
	
	finally:
		print('closing socket')
		sock.close()
