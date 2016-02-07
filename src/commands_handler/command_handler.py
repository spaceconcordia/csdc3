import time
import os
import datetime
import subprocess

class CustomDate:

    def __init__(self, day, month, year, hour, minute, second):
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)
        self.hour = str(hour)
        self.minute = str(minute)
        self.second = str(second)

        # Construct proper date string
        self.dateString = self.day + '/' + self.month + '/' + self.year \
        + ' ' + self.hour + ':' + self.minute + ':' + self.second

        # Validate date string
        datetime.datetime.strptime(self.dateString, '%d/%m/%Y %H:%M:%S')

    def generateDateString(self):
        return self.dateString

class CommandHandler:
    @staticmethod
    def set_system_time(dateObj):
        if dateObj.__class__.__name__ == CustomDate.__name__:
            subprocess.call(['date', '-s', dateObj.generateDateString()])
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
    date = CustomDate(2, 9, 2006, 18, 9, 9)
    print(date.generateDateString())
    # CommandHandler.set_system_time(date)
    print(CommandHandler.get_system_time())
