#!/bin/sh

[ -e /dev/rtc1 ] && return 0;

echo ds3232 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock -s -f /dev/rtc1

timestamp=`cat /sys/class/rtc/rtc1/since_epoch`
if [ "$timestamp" -gt 1465688859 ];
then
  echo success
  break;
else
  echo "$timestamp"
  [ -e /dev/rtc2 ] && return 0;
  echo ds3232 0x68 > /sys/class/i2c-adapter/i2c-0/new_device
  sudo hwclock -s -f /dev/rtc2
fi
