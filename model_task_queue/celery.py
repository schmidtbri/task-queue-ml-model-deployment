"""A task queue for machine learning model deployment."""
import os
from celery import Celery
from celery.app.registry import TaskRegistry

from model_task_queue import __name__
from model_task_queue.ml_model_task import MLModelPredictionTask
import model_task_queue.config as config


# creating a TaskRegistry in order to be able to instantiate a dynamic number of task in the celery app
registry = TaskRegistry()

# instantiating the MLModelPredictionTask objects and adding them to a TaskRegistry object
for model in config.models:
    registry.register(MLModelPredictionTask(module_name=model["module_name"],
                                            class_name=model["class_name"]))

# instantiating the Celery app object
app = Celery(__name__,
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             tasks=registry)

# importing the connection settings
app.config_from_object("model_task_queue.config.{}".format(os.environ['APP_SETTINGS']))
