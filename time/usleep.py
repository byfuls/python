import time

usleep = lambda x: time.sleep(x/1000000.0)
#usleep(100)

start_time = time.time()
usleep(1000)
elapsed_time = time.time() - start_time
print(elapsed_time)
