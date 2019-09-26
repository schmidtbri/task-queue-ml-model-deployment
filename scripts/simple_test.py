"""A script to test the model task queue with a single request"""
import time
from model_task_queue.celery import app


def run_test():

    task = app.tasks["model_task_queue.ml_model_task.iris_model"]

    result = task.delay(data={"sepal_length": 5.0, "sepal_width": 3.2, "petal_length": 1.2, "petal_width": 0.2})

    # waiting for the task to complete
    while result.ready() is not True:
        time.sleep(1)

    prediction = result.get(timeout=1)
    print("The task returned this prediction: {}".format(prediction))


if __name__ == '__main__':
    run_test()
