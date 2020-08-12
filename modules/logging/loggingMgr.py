import logging
import os
import time

class loggingMgr:
    def __init__(self, logDir, logFile):
        # get today
        self.today = time.strftime('%Y%m%d', time.localtime(time.time()))

        # init dir
        self.logFile = logFile
        self.logDir = logDir
        self.todayLogDir = f'{logDir}/log/{self.today}'
        if not os.path.exists(self.todayLogDir):
            os.makedirs(self.todayLogDir)
        self.logFullFile = f'{self.todayLogDir}/{self.logFile}'

        # init log
        self.log = logging.getLogger(__name__)
        #self.format = logging.Formatter('[%(asctime)s][%(levelname)s:%(lineno)s] >> %(message)s')
        self.format = logging.Formatter('[%(asctime)s][%(levelname)s] >> %(message)s')

        #self.streamHandler = logging.StreamHandler()
        self.fileHandler = logging.FileHandler(self.logFullFile)

        #self.streamHandler.setFormatter(self.format)
        self.fileHandler.setFormatter(self.format)

        #self.log.addHandler(self.streamHandler)
        self.log.addHandler(self.fileHandler)

        self.log.setLevel(level=logging.DEBUG)
    def debug(self, msg):
        newDay = time.strftime('%Y%m%d', time.localtime(time.time()))
        if self.today != newDay:
            self.__init__(self.logDir, self.logFile)
        self.log.debug(msg)
    def info(self, msg):
        newDay = time.strftime('%Y%m%d', time.localtime(time.time()))
        if self.today != newDay:
            self.__init__(self.logDir, self.logFile)
        self.log.info(msg)
    def warn(self, msg):
        newDay = time.strftime('%Y%m%d', time.localtime(time.time()))
        if self.today != newDay:
            self.__init__(self.logDir, self.logFile)
        self.log.warning(msg)
    def error(self, msg):
        newDay = time.strftime('%Y%m%d', time.localtime(time.time()))
        if self.today != newDay:
            self.__init__(self.logDir, self.logFile)
        self.log.error(msg)
    def crit(self, msg):
        newDay = time.strftime('%Y%m%d', time.localtime(time.time()))
        if self.today != newDay:
            self.__init__(self.logDir, self.logFile)
        self.log.critical(msg)