import os
import fcntl

class Lock:
    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, 'w')

    def acquire(self):
        fcntl.flock(self.handle, fcntl.LOCK_EX)
        print("Acquired Lock")

    def isLocked(self):
        try:
            fcntl.flock(self.handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return True
        fcntl.flock(self.handle, fcntl.LOCK_UN)
        return False

    def release(self):
        fcntl.flock(self.handle, fcntl.LOCK_UN)
        print("Released Lock")

    def __del__(self):
        self.handle.close()

if __name__ == '__main__':
    try:
        lock = Lock("/home/justin/Desktop/lock.tmp")
        lock.acquire()
    finally:
        lock.release()
