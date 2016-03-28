import _thread as thread,time

def counter(myID,count):
	for i in range(count):
		time.sleep(1)
		print('[%s] => %s '%(myID,i))

for x in range(5):
	thread.start_new_thread(counter,(1,5))
	time.sleep(6)
	print('Main thread exiting.\n')

