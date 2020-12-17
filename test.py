from tzlocal import get_localzone
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
tz = get_localzone()
# print(tz)

# initialize scheduler with your preferred timezone
scheduler = BackgroundScheduler({'apscheduler.timezone': tz})
scheduler.add_jobstore('sqlalchemy', url='sqlite:///data/schedule.db')
scheduler.start()

def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()

time = "2020-12-17T15:24"
date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
text = "test"
#schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
job = scheduler.add_job(printing_something, trigger='date', next_run_time=str(date_time), args=[text])

