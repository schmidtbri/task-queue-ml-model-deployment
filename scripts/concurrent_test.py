"""A script to test the model task queue with a concurrent requests"""
import time
from concurrent.futures import ThreadPoolExecutor as Executor
from model_task_queue.celery import app


def request_task(data):
    task = app.tasks["model_task_queue.ml_model_task.iris_model"]

    result = task.delay(data=data)

    # waiting for the task to complete
    while result.ready() is not True:
        time.sleep(1)

    prediction = result.get(timeout=1)
    return prediction


def run_test():
    data = [
        {"sepal_length": 5.0, "sepal_width": 3.2, "petal_length": 1.2, "petal_width": 0.2},
        {"sepal_length": 5.5, "sepal_width": 3.5, "petal_length": 1.3, "petal_width": 0.2},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1},
        {"sepal_length": 4.4, "sepal_width": 3.0, "petal_length": 1.3, "petal_width": 0.2}
    ]
    with Executor(max_workers=4) as exe:
        jobs = [exe.submit(request_task, d) for d in data]
        results = [job.result() for job in jobs]
        print("The tasks returned these predictions: {}".format(results))


if __name__ == '__main__':
    run_test()
