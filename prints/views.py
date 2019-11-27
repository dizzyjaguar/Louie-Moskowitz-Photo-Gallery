from django.shortcuts import render
from django.http import HttpResponse
from .models import Print
# Create your views here.
def prints(request):
    prints = Print.objects.all().order_by('-date_uploaded')
    context = {
        'prints': prints
    }
    return render(request, 'prints.html', context)
