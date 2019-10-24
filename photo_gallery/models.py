from django.db import models
from django.utils import timezone
from PIL import Image



# figure out how to do this   class Photograph(models.Model):
class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    #location_taken to be made


    def __str__(self):
        return self.title
