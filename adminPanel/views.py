from django.shortcuts import render
from django.urls import reverse # Reverse the function url.
from django.http import HttpResponse, HttpResponseRedirect # Redirect the function urls
from django.contrib.auth import login, logout
from django.contrib import messages # Return messages.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
from adminPanel.EmailBackEnd import EmailBackEnd # Used to login with user email ID.
from django.contrib.auth.hashers import check_password # Check logged-in user password.




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
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("adminPanel:admin-dashboard"))
            elif user.user_type=="2":
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("adminPanel:hr-dashboard"))
            elif user.user_type=="3":
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("adminPanel:staff-dashboard"))
            else:
                messages.success(request, email+" logged in successfully")
                return HttpResponseRedirect(reverse("adminPanel:freelancer-dashboard"))
        else:
            messages.error(request, 'Invalid Logged in details')
            return HttpResponseRedirect(reverse("adminPanel:login"))
    

# This function is used to user logged out.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("adminPanel:login"))


# This function is used to change Admin password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
    return render(request, 'admin-panel/change-password.html')


# This function is used to match admin password.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def match_old_password(request):
    user = request.user
    print(user.password)
    if request.method == 'POST':
        old_password = request.POST['old_password']

    # Check if the current password is valid.
    if not check_password(old_password, user.password):
        messages.error(request, 'Old password is incorrect.')
        return HttpResponseRedirect(reverse('adminPanel:change-password'))
    
    return HttpResponseRedirect(reverse('adminPanel:update-password'))
    

# This function is used to update Admin password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_new_password(request):
    return render(request, 'admin-panel/match-password.html')
    

# This function to update save Admin new password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_save_new_password(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST['new_password']
        new_confirm_password = request.POST['new_confirm_password']
        print(new_password)
        print(new_confirm_password)
        
        # Check if the new password and confirmation match.
        if new_password != new_confirm_password:
            messages.error(request, 'New password do not match.')
            return HttpResponseRedirect(reverse('adminPanel:update-password'))
        
        # Set the new password and update the session auth hash
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully.')
        return HttpResponseRedirect(reverse('adminPanel:login'))
    