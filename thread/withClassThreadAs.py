import threading
import time

class sampleClass(threading.Thread):
    def __init__(self):
        print('[sampleClass] init start')
        super(sampleClass, self).__init__()
        self.threadEvent = threading.Event()

    ### thread method
    # start() or run()
    #def start(self):
    #    print('[sampleClass] start start')
    #    time.sleep(3)
    #    self.threadEvent.set()
    #    print('[sampleClass] thread flag on')
    def run(self):
        print('[sampleClass] run start')
        time.sleep(1)
        self.threadEvent.set()
        print('[sampleClass] thread flag on')
    def join(self):
        print('[sampleClass] join start')
    def close(self):
        print('[sampleClass] close start')
    def stop(self):
        print('[sampleClass] stop start')
    def is_alive(self):
        print(f'[sampleClass] is_alive start: {super().is_alive()}')

    def __enter__(self):
        print('[sampleClass] enter start')
        self.start()
        self.threadEvent.wait()
        print('[sampleClass] thread block free')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('[sampleClass] exit start')

with sampleClass() as sc:
    print('[main] start')
    sc.is_alive()
    print('[main] done')