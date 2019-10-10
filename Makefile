TEST_PATH=./tests

.DEFAULT_GOAL := help

.PHONY: help clean-pyc build clean-build deployment-package venv dependencies test-dependencies clean-venv test test-reports clean-test check-codestyle check-docstyle

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean-pyc: ## Remove python artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

build: ## build a package
	python setup.py sdist bdist_wheel

clean-build:  ## clean build artifacts
	rm -rf build
	rm -rf dist
	rm -rf model_task_queue.egg-info

deployment-package:  ## makes a deployment package with all dependencies
	# installing all dependencies to the vendors directory
	mkdir vendors
	pip install --target vendors -r requirements.txt
	python setup.py sdist --create_deployment_package
	rm -rf vendors
	rm -rf build
	rm -rf model_task_queue.egg-info

venv: ## create virtual environment
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
	venv/bin/pip install --upgrade wheel

dependencies: ## install dependencies from requirements.txt
	pip install -r requirements.txt

test-dependencies: ## install dependencies from test_requirements.txt
	pip install -r test_requirements.txt

clean-venv: ## remove all packages from virtual environment
	pip freeze | grep -v "^-e" | xargs pip uninstall -y

test: clean-pyc ## Run unit test suite.
	pytest --verbose --color=yes $(TEST_PATH)

test-reports: clean-pyc ## Run unit test suite with reporting
	mkdir -p reports
	python -m coverage run --source model_task_queue -m pytest --verbose --color=yes --junitxml=./reports/unit_tests.xml $(TEST_PATH)
	coverage xml -o ./reports/coverage.xml
	rm -rf .coverage

clean-test:	## Remove test artifacts
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf reports

check-codestyle:  ## checks the style of the code against PEP8
	pycodestyle model_task_queue --max-line-length=120

check-docstyle:  ## checks the style of the docstrings against PEP257
	pydocstyle model_task_queue
