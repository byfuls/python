from enum import Enum
import struct

class state(Enum):
    not_connected = 0
    connection_under_negociation = 1

class set_state(Enum):
    idle = 0
    processing_apdu_request = 1

class SAP:
    def __init__(self, socket):
        self.__socket = socket
        self.__parameters = {}
        self.__messages = {}

        def add_parameter_type(name, length, id):
            self.__parameters[id] = {
                'name': name,
                'length': length,
                'id': id
            }

        # populate parameter catalogue
        add_parameter_type("MaxMsgSize",2,0x00)
        add_parameter_type("ConnectionStatus",1,0x01)
        add_parameter_type("ResultCode",1,0x02)
        add_parameter_type("DisconnectionType",1,0x03)
        add_parameter_type("CommandAPDU",-1,0x04)
        add_parameter_type("CommandAPDU7816",2,0x10)
        add_parameter_type("ResponseAPDU",-1,0x05)
        add_parameter_type("ATR",-1,0x06)
        add_parameter_type("CardReaderdStatus",1,0x07)
        add_parameter_type("StatusChange",1,0x08)
        add_parameter_type("TransportProtocol",1,0x09)

        def add_message_type(name, client_to_server, id, parameters):
            params = []
            if len(parameters):
                parameter = parameters[0]
                getParam = self.__parameters.get(id)
                if not getParam:
                    print(f'parameter not found in catalogue: {parameter[0]}')
                else:
                    param = getParam['id']
                    params = [param, parameter[1]]
            self.__messages[name] = {
                'client_to_server': client_to_server,
                'server_to_client': not client_to_server,
                'id': id,
                'parameters': params
            }

        # populate parameter catalogue
        add_message_type("CONNECT_REQ",True,0x00,[[0x00,True]])
        add_message_type("CONNECT_RESP",False,0x01,[[0x01,True],[0x00,False]])
        add_message_type("DISCONNECT_REQ",True,0x02,[])
        add_message_type("DISCONNECT_RESP",False,0x03,[])
        add_message_type("DISCONNECT_IND",False,0x04,[[0x03,True]])
        add_message_type("TRANSFER_APDU_REQ",True,0x05,[[0x04,False],[0x10,False]])
        add_message_type("TRANSFER_APDU_RESP",False,0x06,[[0x02,True],[0x05,False]])
        add_message_type("TRANSFER_ATR_REQ",True,0x07,[])
        add_message_type("TRANSFER_ATR_RESP",False,0x08,[[0x02,True],[0x06,False]])
        add_message_type("POWER_SIM_OFF_REQ",True,0x09,[])
        add_message_type("POWER_SIM_OFF_RESP",False,0x0A,[[0x02,True]])
        add_message_type("POWER_SIM_ON_REQ",True,0x0B,[])
        add_message_type("POWER_SIM_ON_RESP",False,0x0C,[[0x02,True]])
        add_message_type("RESET_SIM_REQ",True,0x0D,[])
        add_message_type("RESET_SIM_RESP",False,0x0E,[[0x02,True]])
        add_message_type("TRANSFER_CARD_READER_STATUS_REQ",True,0x0F,[])
        add_message_type("TRANSFER_CARD_READER_STATUS_RESP",False,0x10,[[0x02,True],[0x07,False]])
        add_message_type("STATUS_IND",False,0x11,[[0x08,True]])
        add_message_type("ERROR_RESP",False,0x12,[])
        add_message_type("SET_TRANSPORT_PROTOCOL_REQ",True,0x13,[[0x09,True]])
        add_message_type("SET_TRANSPORT_PROTOCOL_RESP",False,0x14,[[0x02,True]])

    def create_message(self, msgType, payload=None):
        msg_type = None
        print(f'[test] type:{type(msgType).__name__}')
        if type(msgType).__name__ == "str":
            msg_type = self.__messages.get(msgType)
            print(f'[test] getMessage:{msg_type}')
            if not msg_type:
                raise Exception(f'message type:{type(msgType)} not found')
        else:
            raise Exception(f"TODO, search message via {type(msgType).__name__} type")
        message = msg_type
        print(f'message:{message}')

        message['payload'] = []
        message['payload'] = payload
        print(f'message:{message}, payload:{payload}:{len(payload)}')
        if len(payload):
            param_type = None
            parameter = payload
            if type(parameter[0]).__name__ == 'int':
                param_type = self.__parameters.get(parameter[0])
                print(f'[test] param_type:{param_type}')
                if not param_type:
                    raise Exception(f'param_type:{parameter[0]} not found')
            elif type(parameter[0]).__name__ == 'str':
                raise Exception(f"TODO, search parameters via {type(msgType).__name__} type")
            else:
                raise Exception(f'parameter type {type(parameter[0])} not found')


    def send(self, message):
        pass

if __name__ == "__main__":
    sap = SAP(3)
    payload = []
    connect = sap.create_message("CONNECT_REQ", payload)