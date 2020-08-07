import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
sock.bind(('localhost', 5001))

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print(data)

    if data:
        #sent = sock.sendto(data, address)
        sent = sock.sendto('response'.encode('utf-8'), address)
        print('sent %s bytes back to %s' % (sent, address))
