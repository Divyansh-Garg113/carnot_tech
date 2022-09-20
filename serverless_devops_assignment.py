from apscheduler.schedulers.blocking import BlockingScheduler
import traceback
import datetime
import sys

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', second='0')
def say_hello():
        print("Hello 123", datetime.datetime.utcnow())
if __name__ == '__main__':
        procs = []
        try:
                print("Starting the blocking scheduler")
                scheduler.start()
        except KeyboardInterrupt:
                print('\nExiting by user request.\n', file=sys.stderr)
        except Exception:
                traceback.print_exc(file=sys.stdout)

        sys.exit(0)

def lambda_handle(event, context):
    print("Starting the blocking scheduler, inside lambda_handle() method")
    scheduler.start()
