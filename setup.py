import sys
import os
from os import path
from io import open
from setuptools import setup

from model_etl import ___version__, __doc__

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# this command line option is used when we want to create a deployment package
if "--create_deployment_package" in sys.argv:
    create_deployment_package = True
    sys.argv.remove("--create_deployment_package")
else:
    create_deployment_package = False


def package_files(directory):
    """Create a recursive list of paths to files in a directory"""
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


if create_deployment_package is True:
    # getting the full list of files in the "vendors" folder
    extra_files = package_files(path.abspath(path.join(path.dirname(path.dirname(__file__)), "vendors")))
    # removing files with .pyc, .pyo. and __pycache__ in their path
    extra_files = [s for s in extra_files if ".pyc" not in s and ".pyo" and "__pycache__" not in s]
    parameter_value = {'': extra_files}


setup(
    name='model_etl',
    version=___version__,
    description=__doc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/schmidtbri/etl-job-ml-model-deployment',
    author='Brian Schmidt',
    author_email='6666331+schmidtbri@users.noreply.github.com',
    packages=["model_etl"],
    python_requires='>=3.5',
    install_requires=['bonobo==0.6.4',
                      'fs-s3fs==1.1.1',
                      'iris-model@git+https://github.com/schmidtbri/ml-model-abc-improvements#egg=iris_model@master'],
    package_data={'': []} if create_deployment_package is False else parameter_value
)