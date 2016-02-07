class CronManager:
    @staticmethod
    def update_cron_file(listOfJobs):
        f = open('cronfile_test', 'w')
        for job in listOfJobs:
            if job.__class__.__name__ == CronJob.__name__:
                f.write(job.GenerateCommand())
            else:
                raise TypeError("Invalid date object")
        f.close()

class CronJob:
    def __init__(self, minute, hour, day, month, weekday, command):
        if minute == '*' or 0 <= int(minute) <= 59:
            self.minute = minute
        else:
            raise Exception("Minute out of range")
        if hour == '*' or 0 <= int(hour) <= 23:
            self.hour = hour
        else:
            raise Exception("Hour out of range")
        if day == '*' or 1 <= int(day) <= 31:
            self.day = day
        else:
            raise Exception("Day out of range")
        if month == '*' or 1 <= int(month) <= 12:
            self.month = month
        else:
            raise Exception("Month out of range")
        if weekday == '*' or 0 <= int(weekday) <= 6:
            self.weekday = weekday
        else:
            raise Exception("Weekday out of range")

        self.command = command

    def GenerateCommand(self):
        return self.minute + ' ' + self.hour + ' ' + self.day + \
         ' ' + self.month + ' ' + self.weekday + ' ' + self.command + '\n'

# Overall Structure
# minute (0-59), hour (0-23, 0 = midnight), day (1-31),
# month (1-12), weekday (0-6, 0 = Sunday), command

if __name__ == "__main__":
    jobList = []
    jobList.append(CronJob('1','*','*','*','*', '/root/csdc3/src/custom_gpio.py'))
    jobList.append(CronJob('1','1','1','2','3', '/root/csdc3/src/custom_i2c.py'))
    CronManager.update_cron_file(jobList)
