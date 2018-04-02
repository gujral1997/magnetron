#!/usr/bin/env python
# django-admin startproject magnetron
# python manage.py startapp music
# python manage.py migrate (migrate the changes to the server)
# python manage.py makemigrations music  (tells django than changes in music model has been made)
# python manage.py sqlmigrate music 0001 (what we did in models.py is created in sql format)
# python manage.py shell(special django api based shell)
# Things done in shell
    # from music.models import Album, Song
    # Album.objects.all()
    # a = Album(artist ="Taylor Swift", album_title="Red", genre="Country", album_logo="https://is2-ssl.mzstatic.com/image/thumb/Music/v4/46/55/09/465509be-1cb3-8b41-3282-99ef5f73e92d/12UMGIM54089.jpg/268x0w.jpg")
    # a.save(), then .. a.album_title, a.artist
    # a.id is created automatically
    # b = Album()
    # b.artist = "Myth"
    # Album.objects.filter(id=2)
    # Album.objects.filter(artist__startswith='Taylor')
# python manage.py createsuperuser


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
