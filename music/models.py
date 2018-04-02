from django.db import models

# Create your models here.

# Red primary key 1
class Album(models.Model):
    artist = models.CharFIeld(max_length=250)
    album_title = models.CharFIeld(max_length=500)
    genre = models.CharFIeld(max_length=100)
    album_logo = models.CharFIeld(max_length=1000)

class Song(models.Model):
    album - models.ForeignKey(Album, on_delete=models.CASCADE) # song is linked to album thats y foreign key used
    file_type = models.CharFIeld(max_length=10)
    song_title = models.CharFIeld(max_length=250)
