from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def contact(request):
    return render(request, 'webpages/contact.html')

def aboutus(request):
    return render(request, 'webpages/aboutus.html')

def service(request):
    return render(request, 'webpages/service.html')

def gellary(request):
    return render(request, 'webpages/gellary.html')