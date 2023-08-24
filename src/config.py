import logging
import os
from logging import config

# ENVIRONMENT VARIABLES
ALPHA_URL = os.environ.get("ALPHA_URL", '')
ALPHA_API_KEY = os.environ.get('ALPHA_API_KEY', '')

# LOGGER CONFIG
config.fileConfig('/app/logging.conf')
LOGGER = logging.getLogger('gatewayExample')