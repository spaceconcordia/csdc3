import time
import os
import datetime
import subprocess

class CustomDate:

    # months = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG', \
    # 'SEP', 'OCT', 'NOV','DEC')

    # def __init__(self, day, month, year, hour, minute, second):
    #
    #     if 0 < day <= 31:
    #         self.day = str(day)
    #     else:
    #         raise Exception("Invalid day specified")
    #
    #     if month in self.months:
    #         self.month = month
    #     else:
    #         raise Exception("Invalid month specified")
    #
    #     self.year = str(year)
    #
    #     if 0 < hour <= 24:
    #         self.hour = str(hour)
    #     else:
    #         raise Exception("Invalid hour specified")
    #
    #     if 0 < minute <= 60:
    #         self.minute = str(minute)
    #     else:
    #         raise Exception("Invalid minute specified")
    #
    #     if 0 < second <= 60:
    #         self.second = str(second)
    #     else:
    #         raise Exception("Invalid second specified")

    def __init__(self, dateString):
        # Validate date string
        datetime.datetime.strptime(dateString, '%d/%m/%Y %H:%M:%S')
        self.dateString = dateString

    # def generateDateCommand(self):
    #     return self.day + ' ' + \
    #      self.month + ' ' + self.year + ' ' + \
    #     self.hour + ':' + self.minute + ':' + \
    #     self.second

    def generateDateCommand(self):
        return self.dateString

class CommandHandler:
    @staticmethod
    def set_system_time(dateObj):
        if dateObj.__class__.__name__ == CustomDate.__name__:
            # os.system(dateObj.generateDateCommand)
            subprocess.call(['date', '-s', dateObj.generateDateCommand()])
        else:
            raise TypeError("Invalid date object")

    @staticmethod
    def get_system_time():
        # return time.strftime("%d/%m/%Y %H:%M:%S")
        return subprocess.check_output(['date'])

    @staticmethod
    def start_reboot():
        # os.system('shutdown -r now')
        subprocess.call(['shutdown', '-r', 'now'])

    @staticmethod
    def get_logged_data():
        pass

    @staticmethod
    def delete_logged_data():
        pass

    @staticmethod
    def update_binaries():
        pass

if __name__ == "__main__":
    # date = CustomDate(2, 'OCT', 2006, 18, 9, 9)
    # print(date.generateDateCommand())
    # date = CustomDate('2/6/2016 22:07:13')
    # CommandHandler.set_system_time(date)
    print(CommandHandler.get_system_time())
