import socket
import sys

WAITING_QUEUE_MAX = 10
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')

sock.bind(server_address)
sock.listen(WAITING_QUEUE_MAX)

while True:
	connection, client_address = sock.accept()
	try:
		print(f'connection from: {client_address}')
		while True:
			data = connection.recv(BUFF_SIZE)
			print(f'received data: {data}')
			if data:
				print(f'sending data back to the client')
				connection.sendall(data)
			else:
				print(f'no more data from: {client_address}')
				break
	except Exception as error:
		print(f'error occur when accept client: {error}')
	finally:
		print(f'finally done')
		connection.close()
