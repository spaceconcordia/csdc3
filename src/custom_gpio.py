from ablib import Pin
from time import sleep

led = Pin('J4.7','OUTPUT')
led.on()
sleep(10)
led.off()


