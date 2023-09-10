from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate



# Create your views here.
def dashboard(request):
    return render(request, 'admin-panel/dashboard.html')


def login_page(request):
    return render(request, 'admin-panel/login.html')
    

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)
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