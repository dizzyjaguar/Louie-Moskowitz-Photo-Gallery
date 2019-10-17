from django.db import models
from django.utils import timezone
from PIL import Image



# figure out how to do this   class Photograph(models.Model):
class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    cover_image = models.FilePathField(path="/photo_gallery")


class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.FilePathField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    #location_taken to be made
