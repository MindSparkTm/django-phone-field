#!/usr/bin/env python
import os
import sys

import warnings
from django.utils.deprecation import RemovedInDjango30Warning, RemovedInNextVersionWarning

warnings.filterwarnings('always', category=RemovedInDjango30Warning)
warnings.filterwarnings('always', category=RemovedInNextVersionWarning)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_proj.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
