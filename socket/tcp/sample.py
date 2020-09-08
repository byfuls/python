import multiplexing as sampleTest
import socket

print(f'[sample] 1')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('192.168.242.131', 3001))
server.listen(5)

print(f'[sample] 2')
multiplexingReaderSelect = sampleTest.multiSelect(server)
multiplexingReaderPoll = sampleTest.multiPoll(server)
while True:
    #ret = multiplexingReaderSelect.readRunning(True)
    ret = multiplexingReaderPoll.readRunning(True)
    print(f'[sample] ret: {ret}')
    if ret[0] is sampleTest.EXCEPTIONAL_EVENT:
        break
    if ret[0] is sampleTest.READ_EVENT:
        print(f'[sample] read data: {ret[1]}')

print(f'[sample] ret: {ret}')
