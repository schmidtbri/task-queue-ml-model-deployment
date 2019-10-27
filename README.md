# Task Queue ML Model Deployment
Code to deploy an ML model as a task in a task queue.

This code is used in this [blog post](https://towardsdatascience.com/a-task-queue-ml-model-deployment-552d2ceb38a5).

## Installation 
The makefile included with this project contains targets that help to automate several tasks.

To download the source code execute this command:
```bash
git clone https://github.com/schmidtbri/task-queue-ml-model-deployment
```
Then create a virtual environment and activate it:
```bash

# go into the project directory
cd task-queue-ml-model-deployment

make venv

source venv/bin/activate
```

Install the dependencies:
```bash
make dependencies
```

## Running the unit tests
To run the unit test suite execute these commands:
```bash

# first install the test dependencies
make test-dependencies

# run the test suite
make test
```

## Making a Deployment Package
To create a tarball deployment package for the worker nodes, use this command:
```bash
make deployment-package
```

### Starting a Worker Process
To start a worker process execute these commands:
```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
export APP_SETTINGS=ProdConfig
export PYTHONPATH=./
python3 -m model_task_queue --loglevel INFO
```
