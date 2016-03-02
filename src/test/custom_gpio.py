import sys
sys.path.append('/root/csdc3/lib/ablib')
from ablib_python3 import Pin
from time import sleep


led = Pin('J4.7','OUTPUT')

while 1:
	led.on()
	sleep(2)
	led.off()
	sleep(2)

