from django.contrib import admin

# Register your models here.

from.models import Album, Song

admin.site.register(Album) #registered album in admin site
admin.site.register(Song)
