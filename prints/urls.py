#core django imports
from django.contrib import admin
from django.urls import path
#imports from my apps
from . import views

urlpatterns = [
path('', views.prints, name='prints'),
]
