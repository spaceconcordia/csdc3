from crontab import CronTab

#init cron
cron = CronTab()

#add new cron job
job = cron.new(command='python "Hello World"')

#job settings
job.minutes.every(0.1)
