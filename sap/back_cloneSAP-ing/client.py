import socket
import common

class Client(common.SAP):
    max_msg_size = 0xffff
    def __init__(self, clientSocket):
        super(Client, self).__init__(clientSocket)
        self.__state = common.state.not_connected
        self.__set_state = common.set_state.idle
        self.__clientSocket = clientSocket
    def start(self):
        pass
    def connect(self):
        if self.__state == common.state.connection_under_negociation:
            payload = []
            payload = [0x00, []]
            connect = create_message("CONNECT_REQ", payload)
            send(connect)
            self.__state = common.state.connection_under_negociation
        else:
            raise Exception(f'[sap] can not connect. required state: not_connected, current state: {self.__state}')
    def disconnect(self):
        if self.__state == common.state.connection_under_negociation:
            connect = create_message("DISCONNECT_REQ")
            send(connect)
            self.__state == common.state.not_connected
        else:
            raise Exception(f'[sap] can not disconnect. must be connected, current state: {self.__state}')
    def apdu(self, request):
        if self.__set_state == common.set_state.idle:
            connect = create_message("TRANSFER_APDU_REQ", [[0x04, request]])
            send(connect)
            self.__set_state = common.set_state.processing_apdu_request
            # receive
        else:
            raise Exception(f'[sap] can not send APDU request. must be in state idle, current state: {self.__set_state}')


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9999
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))