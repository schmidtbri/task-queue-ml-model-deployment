"""Simple task queue application that makes predictions with an MLModel class."""
import os
from os import path
import logging
import site

__version_info__ = ('1', '0', '0')
__version__ = '.'.join(__version_info__)

logger = logging.getLogger(__name__)

# adding "vendors" folder as a site directory if it is found in the environment, this allows the application to run
# from a deployment package as well as from a virtual environment with no changes to the code
vendors_path = os.path.join(path.abspath(path.dirname(path.dirname(__file__))), "vendors")
if os.path.exists(vendors_path):
    logger.info("Found a vendors folder at: '{}', adding it as a site directory.".format(vendors_path))
    site.addsitedir(vendors_path)
