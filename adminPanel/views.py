from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    return render(request, 'admin-panel/dashboard.html')


def login(request):
    return render(request, 'admin-panel/login.html')
