#core django imports
from django.urls import path
#imports from my apps
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #!!!!!
    #get the path below to display the gallery title instead of primary key
    path("<int:pk>/", views.gallery_detail, name="gallery_detail"),
    path('about/', views.about, name='about'),
    path('gallery1/', views.gallery1, name='gallery1'),
]
