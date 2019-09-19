"""  """
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')
