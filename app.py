from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timedelta
app = Flask(__name__)

#### get local timezone

from tzlocal import get_localzone
tz = get_localzone()
netherlandstz = "Europe/Amsterdam"
# print(tz)

def printing_something(text):
    print(f"printing {text} at {datetime.now()}")

# initialize scheduler with your preferred timezone
scheduler = BackgroundScheduler({'apscheduler.timezone': netherlandstz})
scheduler.add_jobstore('sqlalchemy', url='sqlite:///data/apscheduler.db')
scheduler.start()

today = datetime.today()
curr_year = int(today.strftime("%Y"))
curr_month = int(today.strftime("%m"))
text = "test txt"

#schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
def addjobs():
    jobs = scheduler.get_jobs()

    for job in jobs:
        scheduler.remove_job(job.id)

    # add test job to run 5 minutes from now
    exec_date = today + timedelta(hours= 7, minutes=5)
    scheduler.add_job(printing_something, trigger='date', next_run_time=str(exec_date), args=[text])

    # add jobs for next month to end of next year     
    for year in range(curr_year,curr_year+2):
        if year == curr_year:
            for month in range(curr_month+1,13):
                exec_date = datetime(year, month, 1)
                scheduler.add_job(printing_something, trigger='date', next_run_time=str(exec_date), args=[text])
        else:
            for month in range(1,13):
                exec_date = datetime(year, month, 1)
                scheduler.add_job(printing_something, trigger='date', next_run_time=str(exec_date), args=[text])
    
    return scheduler.get_jobs()

print(addjobs())

if __name__ == "__main__":
     app.run(host="localhost",debug=True)