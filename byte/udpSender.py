import packetFormat

import socket
import sys

if __name__ == "__main__":
	t = packetFormat.PacketFormating(0)
	t.pkdata = "AS07".encode('utf-8')
	t.pkdata = "510101182682080".encode('utf-8')
	t.pkdata = b'\00\00\00\00\00'
	t.pkdata = b'\00\00\00\00'
	t.pkdata = b'\00\00\00\00'
	print(t.packet)


	# Create a UDP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	server_address = ('localhost', 2220)
	message = t.packet
	
	try:
	    # Send data
	    print("sending '%s'" % message)
	    sent = sock.sendto(message, server_address)
	
	    # Receive response
	    print('waiting to receive')
	    data, server = sock.recvfrom(4096)
	    print("received '%s'" % data)
	
	finally:
	    print('closing socket')
	    sock.close()
