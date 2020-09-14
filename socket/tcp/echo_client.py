import socket
import sys

BUFF_SIZE = 16

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print(f'connecting to {server_address[0]} port {server_address[1]}')

sock.connect(server_address)

try:
	message = 'this is the message. it will be repeated'.encode('utf-8')
	print(f'sending: {message}')
	sock.sendall(message)

	received_len = 0
	received_data = bytes()
	expected_len = len(message)

	while received_len < expected_len:
		data = sock.recv(BUFF_SIZE)
		received_len += len(data)
		received_data += data
		print(f'received length: {data}')
except Exception as error:
	print(f'error occur when accept client: {error}')
finally:
	print(f'stacked received data: {received_data}')
	print(f'closing socket')
	sock.close()
