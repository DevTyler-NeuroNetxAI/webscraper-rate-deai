from apscheduler.schedulers.background import BackgroundScheduler
import auto_update

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(auto_update.main, 'interval', days=1)
    scheduler.start()

# In main.py, add:
# from scheduler import start_scheduler
# start_scheduler()