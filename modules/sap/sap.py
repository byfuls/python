import socket
if __name__ == "__main__":
    import printHexdump as hexdump
import time

'''
[CONNECT_REQ] {:name=>"CONNECT_REQ", :client_to_server=>true, :server_to_client=>false, :id=>0, :parameters=>[[[{:name=>"MaxMsgSize", :length=>2, :id=>0}], true]], :payload=>[{:name=>"MaxMsgSize", :length=>2, :id=>0, :value=>[255, 255]}]}
[TRANSFER_APDU_REQ] {:name=>"TRANSFER_APDU_REQ", :client_to_server=>true, :server_to_client=>false, :id=>5, :parameters=>[[[{:name=>"CommandAPDU", :length=>-1, :id=>4}], false], [[{:name=>"CommandAPDU7816", :length=>2, :id=>16}], false]], :payload=>[{:name=>"CommandAPDU", :length=>-1, :id=>4, :value=>[160, 164, 0, 0, 2, 127, 32]}]}
[ekyoo] pack_message: {:name=>"TRANSFER_APDU_REQ", 
                        :client_to_server=>true,
                        :server_to_client=>false, 
                        :id=>5, 
                        :parameters=>[[[{:name=>"CommandAPDU", :length=>-1, :id=>4}], false], [[{:name=>"CommandAPDU7816", :length=>2, :id=>16}], false]], :payload=>[{:name=>"CommandAPDU", :length=>-1, :id=>4, :value=>[160, 164, 0, 0, 2, 111, 183]}]}
[ekyoo] pack_message: [5, 1, 0, 0, 4, 0, 0, 7, 160, 164, 0, 0, 2, 111, 183, 0]
'''

class sapConv:
    def __init__(self, ip=None, addr=None):
        def packMessage(message):
            # the binary array
            msg_bin = []
            msg_bin.append(message['id'])
            msg_bin.append(len(message['payload'])%0xff)
            msg_bin.extend([0,0])
            #print(f"message: {message['payload']}")
            for parameter in message['payload']:
                #print(f'parameter: {parameter}')
                msg_bin.append(parameter['id'])
                msg_bin.append(0)
                msg_bin.append(len(parameter['value'])//0xff)
                msg_bin.append(len(parameter['value'])%0xff)
                msg_bin.extend(parameter['value'])
                msg_bin.extend([0]*(4-(1+1+2+len(parameter['value']))%4))

            #print(f'msg_bin: {msg_bin}')
            return msg_bin
        self.__packMessage = packMessage
        if ip and addr:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect((ip, addr))
            self.__sockOn = True
        else:
            self.__sockOn = False
    
    def __del__(self):
        self.__socket.close()
    
    def connect(self):
        msg = {
            'id':0,
            'payload':[{'name':"MaxMsgSize", 'length':2, 'id':0, 'value':[255, 255]}]
        }
        convMsg = bytes(self.__packMessage(msg))
        #print(f'convMsg: {convMsg}')
        if self.__sockOn:
            self.__socket.sendall(convMsg)
            head = self.__socket.recv(1024)
            body = self.__socket.recv(1024)
            return
        else:
            return convMsg
    def apdu(self, request):
        msg = {
            'id':5,
            'payload':[{'name':"CommandAPDU", 'length':-1, 'id':4, 'value':request}]
        }
        convMsg = bytes(self.__packMessage(msg))
        if self.__sockOn:
            self.__socket.sendall(convMsg)
            return self.__socket.recv(1024)
        else:
            return convMsg

if __name__ == "__main__":
    try:
        sap = sapConv("127.0.0.1", 1337)
        sap.connect()
        time.sleep(5)
        recv = sap.apdu([160, 164, 0, 0, 2, 127, 32])
        hexdump.print_hex_dump(recv)
        while True:
            time.sleep(1)
    except KeyboardInterrupt as msg:
        print(f'[main] down')
