import time

StatrTime = time.time()
print(time.ctime())
time.sleep(2)

EndTime = time.time()
print(time.ctime())


time.sleep(1)
print(EndTime - StatrTime)
