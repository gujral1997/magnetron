#!/usr/bin/env python
# django-admin startproject magnetron
# python manage.py startapp music
# python manage.py migrate
# python manage.py makemigrations music  (tells django than changes in music model has been made)

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magnetron.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
