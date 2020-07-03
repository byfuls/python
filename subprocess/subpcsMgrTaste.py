import subprocess
import shlex
import time
import select

#################################################################################################################
#ret = subprocess.call("python3 destProcess.py", shell=True)
#print(f'ret: {ret}')
#return : returncode

#################################################################################################################
#ret = subprocess.check_call("python3 destProcess.py", shell=True)
#print(f'ret: {ret}')
#return : returncode

#################################################################################################################
#ret = subprocess.check_output("python3 destProcess.py", shell=True)
#print(f'ret: {ret}')
#return : return byte string

#################################################################################################################
#ret = subprocess.run("python3 destProcess.py", shell=True)
#print(f'ret: {ret}')
# return : CompletedProcess(args='python3 destProcess.py', returncode=0)

#################################################################################################################
#ret = subprocess.Popen(shlex.split("python3 destProcess.py"))
#print(f'ret: {ret}')

#################################################################################################################
#with subprocess.Popen(shlex.split("python3 destProcess.py"), stdout=subprocess.PIPE) as proc:
#    print(proc.poll())
#    print(proc.wait())

#################################################################################################################
#ret = subprocess.Popen(shlex.split("python3 destProcess.py"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#print(f'ret: {ret}, stdout:{ret.stdout} stderr:{ret.stderr} stdin:{ret.stdin}')
##print(f'wait: {ret.wait()}, stdout:{ret.stdout} stderr:{ret.stderr} stdin:{ret.stdin}')
##retcode = ret.poll()
##print(f'poll: {retcode}')
#print(f'poll: {ret.poll()}')
#
#while ret.poll() == None:
#    print(f'while poll: ing, stdout:{ret.stdout}')
#    time.sleep(1)
#print(f'while poll: done, stdout:{ret.stdout}')

#################################################################################################################
class subpObject:
    def __init__(self, fileno, command, uniqueValue):
        self.__fileno = fileno
        self.__command = command
        self.__uniqueValue = uniqueValue
    @property
    def fileno(self):
        return self.__fileno
    @property
    def command(self):
        return self.__command
    @property
    def uniqueValue(self):
        return self.__uniqueValue

subMgr = {}

epoll = select.epoll()
epollCount = 0
subp0 = subprocess.Popen(shlex.split("python3 destProcess.py"), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
epoll.register(subp0.stdout.fileno(), select.EPOLLHUP); epollCount+=1
print(f'[main] epollCount:{epollCount}, stdout:{subp0.stdout.fileno()}')
subMgr[subp0.stdout.fileno()] = subpObject(subp0.stdout.fileno(), "python3 destProcess.py", 0)

subp1 = subprocess.Popen(shlex.split("python3 destProcess.py"), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
epoll.register(subp1.stdout.fileno(), select.EPOLLHUP); epollCount+=1
print(f'[main] epollCount:{epollCount}, stdout:{subp1.stdout.fileno()}')
subMgr[subp1.stdout.fileno()] = subpObject(subp1.stdout.fileno(), "python3 destProcess.py", 1)

print(subMgr)
print(f'[subp0] pid:{subp0.pid}')
print(f'[subp1] pid:{subp1.pid}')

subp0.kill()

#while True:
#    events = epoll.poll(epollCount)
#    for fileno, event in events:
#        print(f"[main] event occur, fileno:{fileno} event:{event}")
#        who = subMgr.get(fileno)
#        print(f'[main] searched fileno:{fileno}, fileno:{who.fileno} command:{who.command} uniqueValue:{who.uniqueValue}')
#
#        # again
#        aga = subprocess.Popen(shlex.split(who.command), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#        epoll.register(aga.stdout.fileno(), select.EPOLLHUP)
#        subMgr[aga.stdout.fileno()] = subpObject(aga.stdout.fileno(), who.command, who.uniqueValue)
#
#        # delete
#        del subMgr[fileno]
#        epoll.unregister(fileno)
#        break