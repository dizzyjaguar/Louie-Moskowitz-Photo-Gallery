from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:pk>/", views.gallery_detail, name="gallery_detail"),
    path('about/', views.about, name='about'),
    path('gallery1/', views.gallery1, name='gallery1'),
]
