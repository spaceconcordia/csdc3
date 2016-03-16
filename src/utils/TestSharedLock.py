from multiprocessing import Process
from time import sleep
from SharedLock import Lock

"""
The goal of this file is to test the locking behaviour of SharedLock
"""

def f(i):
	l = Lock("/home/justin/Desktop/lock.tmp")
	l.acquire()
	try:
		print('Thread', i, 'has lock')
		sleep(2)
	finally:
		l.release()

def checkLock():
    l = Lock("/home/justin/Desktop/lock.tmp")
    if l.isLocked():
        print("Lock is locked")
    else:
        print("Lock is NOT locked")

if __name__ == '__main__':
    l = Lock("/home/justin/Desktop/lock.tmp")
    checkLock()
    sleep(1)
    Process(target=f, args=(1,)).start()
    sleep(1)
    checkLock()
    Process(target=f, args=(2,)).start()
    sleep(7)
    checkLock()
