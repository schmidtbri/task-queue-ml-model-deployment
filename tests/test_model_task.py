import unittest

from model_task_queue.ml_model_task import MLModelPredictionTask


# creating a mockup class to test with
class SomeClass(object):
    pass


class ModelManagerTests(unittest.TestCase):

    def test1(self):
        """ testing the MLModelPredictionTask class with good data """
        # arrange
        model_task = MLModelPredictionTask(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        result = None
        try:
            result = model_task.run(data={"sepal_length": 4.4, "sepal_width": 2.9, "petal_length": 1.4, "petal_width": 0.2})
        except Exception as e:
            exception_raised = True

        # assert
        self.assertFalse(exception_raised)
        self.assertTrue(type(result) is dict)

    def test2(self):
        """ testing the MLModelPredictionTask class with data with incorrect schema """
        # arrange
        model_task = MLModelPredictionTask(module_name="iris_model.iris_predict", class_name="IrisModel")

        # act
        exception_raised = False
        result = None
        try:
            result = model_task.run(data={"sepal_length": 4.4, "sepal_width": 2.9, "petal_width": 0.2})
        except Exception as e:
            exception_raised = True

        # assert
        self.assertTrue(exception_raised)
        self.assertTrue(result is None)

    def test3(self):
        """ testing that the MLModelPredictionTask only allows MLModel objects to be stored """
        # arrange, act
        # using the class defined at the top of this file to test
        exception_raised = False
        exception_message = ""
        try:
            model_task = MLModelPredictionTask(module_name="tests.test_model_task", class_name="SomeClass")
        except Exception as e:
            exception_raised = True
            exception_message = str(e)

        # assert
        self.assertTrue(exception_raised)
        self.assertTrue(exception_message == "MLModelPredictionTask can only be used with subtypes of MLModel.")


if __name__ == '__main__':
    unittest.main()
