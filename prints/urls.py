#core django imports
from django.contrib import admin
from django.urls import path
#imports from my apps
from . import views
from .views import printEmail, successView

urlpatterns = [
path('prints/', views.prints, name='prints'),
path('inquiry/', printEmail, name='inquiry'),
path('prints/<int:print_id>', views.print_detail, name='print-detail'),
]
