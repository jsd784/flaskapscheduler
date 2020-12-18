from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
app = Flask(__name__)


#### get local timezone

from tzlocal import get_localzone
tz = get_localzone()
# print(tz)

def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))

# initialize scheduler with your preferred timezone
scheduler = BackgroundScheduler({'apscheduler.timezone': tz})
scheduler.add_jobstore('sqlalchemy', url='sqlite:///data/apscheduler.db')
scheduler.start()
# time = "2020-12-17T15:34"

timelst = ["2020-12-17T15:37","2020-12-17T15:38","2020-12-17T15:39","2020-12-17T15:41","2020-12-17T17:05"]

text = "test"
#schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
def addjobs(chk):
    if chk == 1:
        return "Jobs Already added"
    else:
        for time in timelst:
            date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
            if date_time > datetime.now():
                job = scheduler.add_job(printing_something, trigger='date', next_run_time=str(date_time), args=[text])
        chk = 1
        return "Success"

#initialize with 0 


# add flask first_time_run only or initi -----
# addjobs(0)

# print(scheduler.get_jobs())

if __name__ == "__main__":
     app.run(host="localhost",debug=True)