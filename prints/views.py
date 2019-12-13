from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Print
from .forms import PrintForm
# Create your views here.
def prints(request):
    prints = Print.objects.all().order_by('-date_uploaded')
    context = {
        'prints': prints
    }
    return render(request, 'prints.html', context)

def print_detail(request, print_id):
    print_object = Print.objects.get(pk=print_id)
    context = {
        'print_object': print_object
    }
    return render(request, 'print_detail.html', context)

def printEmail(request):
    if request.method == 'GET':
        form = PrintForm()
    else:
        form = PrintForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dizzyjaguar@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "inquiry.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for the message.')
