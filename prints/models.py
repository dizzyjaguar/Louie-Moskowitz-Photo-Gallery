from django.db import models
from django.utils import timezone
from PIL import Image

class Print(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='prints')


    def __str__(self):
        return self.title
