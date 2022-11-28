from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import count_pending_questions


sched = BlockingScheduler()
sched.add_job(count_pending_questions, 'cron', day_of_week='mon-fri', hour='9-18', minute=1)
sched.add_job(count_pending_questions, 'cron', day_of_week='mon-fri', hour='9-18', minute=2)
sched.add_job(count_pending_questions, 'cron', day_of_week='mon-fri', hour='9-18', minute=3)
sched.add_job(count_pending_questions, 'cron', day_of_week='mon-fri', hour='9-18', minute=4)

sched.start()