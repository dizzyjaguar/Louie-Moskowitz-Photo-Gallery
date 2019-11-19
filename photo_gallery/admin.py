#core django imports
from django.contrib import admin
from django.utils.safestring import mark_safe
#imports from my app
from .models import Album, Photo

class PhotoAdmin(admin.ModelAdmin):

    readonly_fields = ["photo"]
    list_display = ['title', 'description']
    def photo(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width / 6,
            height=obj.image.height / 6,
            )
    )

class AlbumAdmin(admin.ModelAdmin):

    readonly_fields = ["photo"]
    list_display = ['title', 'description']
    def photo(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.cover_image.url,
            width=obj.cover_image.width / 6,
            height=obj.cover_image.height / 6,
            )
    )

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)

#CREATE SUPERUSER TO GET INTO admin
#SETUP SO ADMIN CREATES ALBUMS AND PHOTOS
