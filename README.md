# Task Queue ML Model Deployment
Code to deploy an ML model as a task in a task queue.

This code is used in this [blog post]().

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

## Commands to install packages to compile librabbitmq

From [here](https://github.com/celery/librabbitmq/issues/123).

```bash
brew install autoconf
brew install automake
brew install pkg-config
brew install libtool
```
