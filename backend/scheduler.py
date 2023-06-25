from apscheduler.schedulers.background import BackgroundScheduler
from .main import app

scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda: app.test_client().get('/data'),trigger='interval',days=1)

scheduler.start()