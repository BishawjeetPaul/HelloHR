from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
from adminPanel.EmailBackEnd import EmailBackEnd



# Create your views here.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'admin-panel/dashboard.html')


def login_page(request):
    return render(request, 'admin-panel/login.html')
    

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/adminPanel/dashboard/")
        else:
            return HttpResponse("Invalid Login")
        

def GetUserDetail(request):
    if request.user!=None:
        return HttpResponse("Username : "+request.user.username+" userType : "+request.user.user_type)
    else:
        return HttpResponse("Please Login first")
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/adminPanel/login/')


def create_user(request):
    return render(request, 'admin-panel/account/create-user.html')