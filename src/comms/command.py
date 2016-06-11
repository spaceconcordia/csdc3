import sys
import os
from time import time
import subprocess

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
        return output

    def execute(self):
        print "[FIRE] SetTime command"
        if self.isArmed:
            print "[SUCCESS] SetTime command"
            print "date -s @%d" % self.time
            os.system("date -s @%d" % self.time)
            os.system("hwclock -w")
            output = subprocess.check_output("date", shell=True)

        else:
            print "[ABORT] SetTime command was not armed. Failed to execute"
            output = "[ABORT] SetTime command was not armed. Failed to execute"

        self.isArmed = False
        return output

    def cancel(self):
        print "[CANCEL] SetTime command"
        self.isArmed = False

COMMANDS = {'settime': SetTimeCommand()}

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
            print "[ERROR] Command not found: %s" % cmd

if __name__ == "__main__":
    main()
