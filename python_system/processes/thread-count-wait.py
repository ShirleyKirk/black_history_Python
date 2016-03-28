import _thread as thread,time
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myID,count):
	for i in range(count):
		time.sleep(1)
		stdoutmutex.acquire()
		print('[%s] => %s '%(myID,i))
		stdoutmutex.release()
	exitmutexes[myID].acquire() #向主线程发送信号。

for i in range(10):
	thread.start_new_thread(counter,(i,100))

for mutex in exitmutexes:
	while not mutex.locked():
		pass

####time.sleep(6)
print('Main thread exiting.\n')

