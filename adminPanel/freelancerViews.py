from django.shortcuts import render #Used to render the .html pages.
from django.contrib.auth.hashers import check_password # Check logged-in user password.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
from django.urls import reverse # Reverse the function url.
from django.http import HttpResponseRedirect # Redirect the function url.
from django.contrib import messages # Return messages.




# This function is used to freelancer dashboard.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'freelancer-panel/dashboard.html')


# This function is used to freelancer candidate submission.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate_submission(request):
    return render(request, "freelancer-panel/candidate-submission.html")


# This function is used to change freelancer password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
    return render(request, 'freelancer-panel/change-password.html')


# This function is used to match freelancer password.
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def match_old_password(request):
    user = request.user

    if request.method == 'POST':
        old_password = request.POST['old_password']

    # Check if the current password is valid.
    if not check_password(old_password, user.password):
        messages.error(request, 'Old password is incorrect.')
        return HttpResponseRedirect(reverse('adminPanel:freelancer-change-password'))
    
    return HttpResponseRedirect(reverse('adminPanel:freelancer-update-password'))
    

# This function is used to update staff password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_new_password(request):
    return render(request, 'freelancer-panel/match-password.html')
    

# This function to update save staff new password:
@login_required(login_url="adminPanel:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_save_new_password(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST['new_password']
        new_confirm_password = request.POST['new_confirm_password']
        
        # Check if the new password and confirmation match.
        if new_password != new_confirm_password:
            messages.error(request, 'New password do not match.')
            return HttpResponseRedirect(reverse('adminPanel:freelancer-update-password'))
        
        # Set the new password and update the session auth hash
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully.')
        return HttpResponseRedirect(reverse('adminPanel:freelancer-dashboard'))
