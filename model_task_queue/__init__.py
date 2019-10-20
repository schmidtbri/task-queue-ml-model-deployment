"""Simple task queue application that makes predictions with an MLModel class."""
import os
import sys
import logging

__version_info__ = ('1', '0', '0')
__version__ = '.'.join(__version_info__)

logger = logging.getLogger(__name__)

# adding "vendors" folder as a site directory if it is found in the environment, this allows the application to run
# from a deployment package as well as from a virtual environment with no changes to the code
vendors_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "vendors")
if os.path.exists(vendors_path):
    sys.path = [vendors_path] + sys.path
    logger.info("Found a vendors folder at: '{}', adding it to the python path.".format(vendors_path))
