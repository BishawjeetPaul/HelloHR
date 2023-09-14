from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages # Return messages.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
from adminPanel.EmailBackEnd import EmailBackEnd




# This function is used to user logged in page.
def login_page(request):
    return render(request, 'admin-panel/login.html')
    

# This function is used to get user logged in.
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            if user.user_type=="1":
                messages.succerss(request, email+" logged in successfully")
                return HttpResponseRedirect("/hellohr/admin/dashboard/")
            elif user.user_type=="2":
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("hr-dashboard"))
            elif user.user_type=="3":
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("staff-dashboard"))
            else:
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("freelancer-dashboard"))
        else:
            messages.error(request, 'Invalid Logged in details')
            return HttpResponseRedirect("/hellohr/login/")
        

# This function is used to get user details.
def GetUserDetail(request):
    if request.user!=None:
        return HttpResponse("Username : "+request.user.username+" userType : "+request.user.user_type)
    else:
        return HttpResponse("Please Login first")
    

# This function is used to user logged out.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))