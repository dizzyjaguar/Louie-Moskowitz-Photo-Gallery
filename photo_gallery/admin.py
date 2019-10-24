from django.contrib import admin
from .models import Album, Photo


admin.site.register(Album)
admin.site.register(Photo)
#CREATE SUPERUSER TO GET INTO admin
#SETUP SO ADMIN CREATES ALBUMS AND PHOTOS
