import sys
sys.path.append('/root/csdc3/src/cron')
from time import time
from cron_manager import *
import subprocess
import os

PREFIX = '[CDH]'

class Command:
    def __init__(self):
        self.isArmed = False

    def arm(self, *args):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

class SetTimeCommand(Command):
    def arm(self, *args):
        try:
            if None not in args:
                self.time = int(args[0])
                self.isArmed = True
                output = "[ARM] SetTime to %d" % self.time
            else:
                output = "[ERROR] Invalid time specified"
        except:
            output = "[ERROR] Invalid time specified"
        print PREFIX+output
        return PREFIX+output

    def execute(self):
        print "[FIRE] SetTime command"
        if self.isArmed:
            print "[SUCCESS] SetTime command"
            #print "date -s @%d" % self.time
            os.system("date -s @%d" % self.time)
            os.system("hwclock -w -f /dev/rtc1")
            os.system("hwclock -w -f /dev/rtc2")
            output = subprocess.check_output("date", shell=True)

        else:
            output = "[ABORT] SetTime command was not armed. Failed to execute"

        self.isArmed = False
        print PREFIX+output
        return PREFIX+output

    def cancel(self):
        print "[CANCEL] SetTime command"
        self.isArmed = False

class SchedulePayloadCommand(Command):
    def arm(self, *args):
        try:
            if None not in args:
                self.args = args[0].split(':')
                if len(self.args) == 4:
                    runmin   = self.args[0]
                    runhr    = self.args[1]
                    runday   = self.args[2]
                    runmonth = self.args[3]

                    self.cron = CronManager()
                    testpayload = "/root/csdc3/src/payload/payload.sh"

                    self.cron.add_or_update_job('*',            \
                                                '*',            \
                                                '*',            \
                                                '*',            \
                                                '*',            \
                                                'python /root/csdc3/src/sensors/sensor_sweep.py')

                    self.cron.add_or_update_job(int(runmin),    \
                                                int(runhr),     \
                                                int(runday),    \
                                                int(runmonth),  \
                                                '*',            \
                                                testpayload)

                    output = "[ARM] \'%s\' scheduled at %s" % (testpayload, self.args)
                    self.isArmed = True
                else:
                    output = "[ERROR] SchedulePayload has invalid parameters specified"
            else:
                output = "[ERROR] SchedulePayload needs parameters"
        except:
            output = "[ERROR] SchedulePayload invalid parameters specified"
        print PREFIX+output
        return PREFIX+output

    def execute(self):
        runmin   = self.cron.jobList[1]['minute']
        runhr    = self.cron.jobList[1]['hour']
        runday   = self.cron.jobList[1]['day']
        runmonth = self.cron.jobList[1]['month']
        output   = '[SUCCESS] Payload scheduled for %s-%s-%s-%s' % \
                                  (runmin, runhr, runday, runmonth)
        self.cron.update_cron_file()
        print PREFIX+output
        return PREFIX+output

    def cancel(self):
        print "[CANCEL] SetTime command"
        self.isArmed = False

COMMANDS = {'settime': SetTimeCommand(),
            'schedpayload': SchedulePayloadCommand()}

def main():
    command = None
    while True:
        gnd_command = raw_input("enter satellite command: ")
        cmd_parsed = gnd_command.split(' ')
        cmd = cmd_parsed[0]
        try:
            if cmd == '!' and command is not None:
                command.execute()
            else:
                command = COMMANDS[cmd]
                params = None
                if len(cmd_parsed) > 1:
                    params = cmd_parsed[1]
                command.arm(params)
        except KeyError:
            print PREFIX+"[ERROR] Command not found: %s" % cmd

if __name__ == "__main__":
    main()
