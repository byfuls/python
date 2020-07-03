import subprocess
import shlex
import time
import select

class processManager():
    class processDataObject:
        def __init__(self, fileno, command, no):
            self._fileno = fileno
            self._command = command
            self._no = no

    def __init__(self):
        super(processManager, self).__init__()
        self.__dict = {}

if __name__ == "__main__":
    mgr = processManager()