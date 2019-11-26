from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def prints(request):
    return render(request, 'prints.html', {})
