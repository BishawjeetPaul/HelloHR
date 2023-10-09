from django.shortcuts import render # Used to render the .html pages.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
from django.contrib.auth.hashers import check_password # Check the loged-in user password.
from django.urls import reverse # Reverse the function url.
from django.http import HttpResponseRedirect # Redirect the function url.
from django.contrib import messages # Return messages.





# This function is used to hr dashboard.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'hr-panel/dashboard.html')


# This function is used to showing candidate details.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate_detail(request):
    return render(request, "hr-panel/candidate-detail.html")


# This function is used to manage canditates.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate_manage(request):
    return render(request, "hr-panel/candidate-manage.html")


# This function is used to select candidates.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate_selected(request):
    return render(request, "hr-panel/candidate-selected.html")


# This function is used to reject candidates.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate_rejected(request):
    return render(request, "hr-panel/candidate-rejected.html")


# This function is used to change hr password.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
    return render(request, 'hr-panel/change-password.html')


# This function is used to match hr password.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def match_old_password(request):
    user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')

        # Check if the current password is valid.
        if not check_password(old_password, user.password):
            messages.error(request, 'Old password is incorrect.')
            return HttpResponseRedirect(reverse('adminPanel:hr-change-password'))
    
        return HttpResponseRedirect(reverse('adminPanel:hr-update-password'))


# This function is used to update Admin password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_new_password(request):
    return render(request, 'hr-panel/match-password.html')


# This function is used to save update password.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_save_new_password(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        new_confirm_password = request.POST.get('new_confirm_password')
        
        # Check if the new password and confirmation match.
        if new_password != new_confirm_password:
            messages.error(request, 'New password do not match.')
            return HttpResponseRedirect(reverse('adminPanel:hr-update-password'))
        
        # Set the new password and update the session auth hash
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully.')
        return HttpResponseRedirect(reverse('adminPanel:login'))