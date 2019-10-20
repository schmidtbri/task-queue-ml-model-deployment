"""Main entry point for the Celery worker process.

..note::
    This script is here to start a worker process from the deployment package.

"""
import sys
from model_task_queue.celery import app


if __name__ == "__main__":
    # starting the Celery app in worker mode
    app.start(argv=['celery', 'worker'] + sys.argv[1:])
