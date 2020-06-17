import select, socket

ACCEPT_EVENT = 0
READ_EVENT = 1
WRITE_EVENT = 2
EXCEPTIONAL_EVENT = 3

class multiSelect():
    def __init__(self, serverSock, timeout=5):
        self.__readable = 0
        self.__writable = 0
        self.__exceptional = 0

        self.__inputs = list()
        self.__outputs = list()
        self.__serverSock = serverSock
        self.__timeout = timeout

        self.__inputs.append(self.__serverSock)
        return
    
    def readRunning(self, __DEBUGGING=False):
        # return code
        # 0 : accept event
        # 1 : read event
        # 2 : write event 
        # 3 : exception event
        while self.__inputs:
            self.__readable, self.__writable, self.__exceptional = \
                select.select(self.__inputs, self.__outputs, self.__inputs, self.__timeout)
            for s in self.__readable:
                if __DEBUGGING:
                    print(f'[readRunning] get in readable')
                if s is self.__serverSock:
                    connection, clientAddress = s.accept()
                    connection.setblocking(0)
                    self.__inputs.append(connection)
                    if __DEBUGGING:
                        print(f'[readRunning] accept new, addr:{clientAddress}')
                    return (ACCEPT_EVENT, clientAddress)
                else:
                    data = s.recv(1024)
                    if data:
                        if __DEBUGGING:
                            print(f'[readRunning] read data: {data}')
                        if s not in self.__outputs:
                            self.__outputs.append(s)
                        return (READ_EVENT, data)
                    else:
                        if __DEBUGGING:
                            print(f'[readRunning] read disconnection')
                        if s in self.__outputs:
                            self.__outputs.remove(s)
                        self.__inputs.remove(s)
                        s.close()
            
            # [todo]
            #for s in self.__writable:
            #    try:
            #        s.send(data)
            #    except Exception as msg:
            #        return msg
            
            for s in self.__exceptional:
                if __DEBUGGING:
                    print(f'[readRunning] exceptional event occur')
                self.__inputs.remove(s)
                if s in self.__outputs:
                    self.__outputs.remove(s)
                s.close()
                return (EXCEPTIONAL_EVENT, "exception err")