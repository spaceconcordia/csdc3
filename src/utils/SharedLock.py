import os
import fcntl

class Lock:
    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, 'w')

    def acquire(self):
        fcntl.flock(self.handle, fcntl.LOCK_EX)
        print("Acquired Lock")

    def acquireNonBlocking(self):
        if self.isLocked():
            return False
        self.acquire()
        return True

    def isLocked(self):
        try:
            fcntl.flock(self.handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return True
        fcntl.flock(self.handle, fcntl.LOCK_UN)
        return False

    def release(self):
        if self.isLocked():
            fcntl.flock(self.handle, fcntl.LOCK_UN)
            print("Released Lock")
        else:
            print("Lock not yet acquired")

    def __del__(self):
        self.handle.close()

if __name__ == '__main__':
    try:
        lock = Lock("/home/justin/Desktop/lock.tmp")
        lock.acquire()
    finally:
        lock.release()
