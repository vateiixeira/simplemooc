from django.shortcuts import render
from .mail import send_mail_template
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
