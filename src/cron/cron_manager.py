class CronManager:
    def __init__(self):
        self.jobList = []

    def update_cron_file(self):
        """
        Method for updating cron file, based on
        the contents of the list.
        """
        # f = open('/var/spool/cron/crontabs/cronfile_test', 'w')
        f = open('C:\Users\justi\Desktop\cronfile_test', 'w')
        for job in self.jobList:
            f.write(self.generate_command(job))
        f.close()

    def generate_command(self, job):
        return job['minute'] + ' ' + job['hour'] + ' ' + job['day'] + \
         ' ' + job['month'] + ' ' + job['weekday'] + \
         ' ' + job['command'] + '\n'

    def add_or_update_job(self, minute, hour, day, month, weekday, command):
        """
        Method for adding jobs. If the job is already added,
        the schedule for this job will be updated.
        """
        if not (minute == '*' or 0 <= int(minute) <= 59):
            raise Exception("Minute out of range")
        if not (hour == '*' or 0 <= int(hour) <= 23):
            raise Exception("Hour out of range")
        if not (day == '*' or 1 <= int(day) <= 31):
            raise Exception("Day out of range")
        if not (month == '*' or 1 <= int(month) <= 12):
            raise Exception("Month out of range")
        if not (weekday == '*' or 0 <= int(weekday) <= 6):
            raise Exception("Weekday out of range")

        # Check if the job already exists, if yes then remove.
        for job in self.jobList:
            if job['command'] == command:
                self.jobList.remove(job)

        # Add new job to list
        job = {'minute': minute, 'hour': hour, 'day': day, \
        'month': month, 'weekday': weekday, 'command': command}

        self.jobList.append(job)

    def remove_job(self, command):
        """
        Method for removing existing jobs.
        """
        isJobFound = False
        for job in self.jobList:
            if job['command'] == command:
                self.jobList.remove(job)
                isJobFound = True

        if not isJobFound:
            raise Exception('Job does not exist and cannot be removed.')


if __name__ == "__main__":
    cronManager = CronManager()
    cronManager.add_or_update_job('1','*','*','*','*', 'python3 /root/csdc3/src/custom_gpio.py')
    cronManager.add_or_update_job('1','1','1','2','3', 'python3 /root/csdc3/src/custom_i2c.py')
    cronManager.add_or_update_job('1','1','1','2','5', 'python3 /root/csdc3/src/custom_i2c.py')
    # cronManager.remove_job('python3 /root/csdc3/src/custom_gpio.py')
    cronManager.update_cron_file()
