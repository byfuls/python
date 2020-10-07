import threading
import socket
import time
import packetFormat

BUFFER_SIZE = 1024

class commThread(threading.Thread):
    def __init__(self, host, port):
        super(commThread, self).__init__()

        try:
            svrAddr = (host, port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(svrAddr)
        except Exception:
            print('tcp connect error');
            exit(1)

        self.__sock = sock
        self.start()

    def __del__(self):
        pass

    def start(self):
        self.__sender = threading.Thread \
                        (target=self.t_sender, args=(self.__sock,))
        self.__receiver = threading.Thread \
                          (target=self.t_receiver, args=(self.__sock,))
        self.__sender.start()
        self.__receiver.start()
    
    def t_sender(self, sock):
        pk = packetFormat.PacketFormating(0)
        pk.pkdata = bytearray('CONID', 'utf8')
        while True:
            s_val = input("SMS Sending Message: ")
        
    def t_receiver(self, sock):
        while True:
            print('receiver ...');
            time.sleep(1)

if __name__ == "__main__":
    try:
        mgr = commThread('127.0.0.1', 20200)
    except KeyboardInterrupt:
        print('done')
        exit(1)
