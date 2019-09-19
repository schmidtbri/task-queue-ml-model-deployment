"""  """
from celery import Task


class MLModelPredictionTask(Task):
    """  """
    def __init__(self):
        self._model = None

    def run(self, data):
        try:
            return self._model.predict(data=data)
        except KeyError:
            return False
