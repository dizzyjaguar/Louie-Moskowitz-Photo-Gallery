from django.shortcuts import render
from django.http import HttpResponse
from photo_gallery.models import Album, Photo

def home(request):
    albums = Album.objects.all().order_by('-date_uploaded')
    context = {
        "albums": albums
    }
    return render(request, 'photo_gallery/home.html', context)


#attempt to make model specific gallery page
def gallery_detail(request, pk):
    album = Album.objects.get(pk=pk)
    photos = Photo.objects.filter(album=album)  #this is probably wrong, look into how to get the specific photos for the album to show up
    context = {
        'album': album,
        'photos': photos
    }
    return render(request, 'photo_gallery/gallery_detail.html', context)




def about(request):
    return render(request, 'photo_gallery/about.html', {})

def gallery1(request):
    return render(request, 'photo_gallery/gallery1.html', {})
# Create your views here.
