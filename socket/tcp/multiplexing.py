import select, socket

ACCEPT_EVENT = 0
READ_EVENT = 1
WRITE_EVENT = 2
DISCONNECT_EVENT = 3
EXCEPTIONAL_EVENT = 4

class multiEPoll():
    def __init__(self, serverSock, timeout=5, defaultBufferSize=1024):
        self.__timeout = timeout
        self.__defaultBufferSize = defaultBufferSize
        self.__serverSock = serverSock
    def __del__(self):
        self.__serverSock.close()
    
    def readRunning(self, __DEBUGGING=False):
        while True:
            pass

class multiPoll():
    def __init__(self, serverSock, timeout=5, defaultBufferSize=1024):
        self.__timeout = timeout
        self.__defaultBufferSize = defaultBufferSize
        self.__serverSock = serverSock
        self.__poll = select.poll()
        self.__poll.register(self.__serverSock, (select.POLLIN | select.POLLPRI))
        self.__socketObjects = {}
    def __del__(self):
        self.__serverSock.close()
    
    def readRunning(self, __DEBUGGING=False):
        while True:
            events = self.__poll.poll(self.__timeout)
            for fd, event in events:
                if __DEBUGGING:
                    print(f'[readRunning] recevied event, svr:{self.__serverSock} fd:{fd} event:{event}')
                if event == select.POLLIN or event == select.POLLPRI:
                    if fd == self.__serverSock.fileno():
                        connection, clientAddress = self.__serverSock.accept()
                        connection.setblocking(0)
                        self.__poll.register(connection.fileno(), (select.POLLIN | select.POLLPRI))
                        self.__socketObjects[connection.fileno()] = connection
                        if __DEBUGGING:
                            print(f'[readRunning] accept new, fd:{connection.fileno()} addr:{clientAddress}')
                            print(f'[readRunning] socket objects:{len(self.__socketObjects)}')
                    else:
                        sockObj = self.__socketObjects.get(fd)
                        data = sockObj.recv(self.__defaultBufferSize)
                        if data:
                            if __DEBUGGING:
                                print(f'[readRunning] read data: {data}')
                                print(f'[readRunning] socket objects:{len(self.__socketObjects)}')
                            return (READ_EVENT, data)
                        else:
                            if fd in self.__socketObjects:
                                (self.__socketObjects[fd]).close()
                                del(self.__socketObjects[fd])
                                self.__poll.unregister(fd)
                            if __DEBUGGING:
                                print(f'[readRunning] read disconnection')
                                print(f'[readRunning] socket objects:{len(self.__socketObjects)}')
                            return (DISCONNECT_EVENT, fd)
                elif event == select.POLLOUT:
                    print(f'[readRunning] ready for output is not supported not')
                    pass
                else:
                    print(f'[readRunning] event:{event} occur, socket will be closed')
                    if fd in self.__socketObjects:
                        (self.__socketObjects[fd]).close()
                        del(self.__socketObjects[fd])
                        self.__poll.unregister(fd)
                    if __DEBUGGING:
                        print(f'[readRunning] socket objects:{len(self.__socketObjects)}')
                    return (EXCEPTIONAL_EVENT, event)

class multiSelect():
    def __init__(self, serverSock, timeout=5, defaultBufferSize=1024):
        self.__readable = 0
        self.__writable = 0
        self.__exceptional = 0

        self.__inputs = list()
        self.__outputs = list()
        self.__serverSock = serverSock
        self.__timeout = timeout
        self.__defaultBufferSize = defaultBufferSize

        self.__inputs.append(self.__serverSock)
    def __del__(self):
        self.__serverSock.close()
    
    def readRunning(self, __DEBUGGING=False):
        # return code
        # 0 : accept event
        # 1 : read event
        # 2 : write event 
        # 3 : disconnect event
        # 4 : exception event
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
                    data = s.recv(self.__defaultBufferSize)
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
                        return (DISCONNECT_EVENT, s)
            
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