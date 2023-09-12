from django.shortcuts import render #Used to render the .html pages.
from . models import CustomUser, CompanyHR # From models.py.
from django.contrib import messages # Return messages.
from django.http import HttpResponseRedirect # Redirect the pages.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
import random # Generated random numbers.




# Function to create page CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_company_hr(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     file = request.FILES['file']

    #     company_hr = CompanyHR.objects.create(
    #         name=name,
    #         phone=phone,
    #         email=email,
    #         subject=subject,
    #         message=message,
    #         file=file
    #     )
    #     company_hr.save()
    #     messages.success(request, 'Message sent successfully..!')
    #     return HttpResponseRedirect('/')
    return render(request, 'admin-panel/create-companyhr.html')


# Function to save CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_company_hr(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('first_name')
        email = request.POST.get('first_name')
        username = request.POST.get('username')
        mobile_no = request.POST.get('first_name')
        address = request.POST.get('first_name')
        gender = request.POST.get('first_name')
        password = request.POST.get('password')
        birth_date = request.POST.get('first_name')

        check_company_hr = CompanyHR.objects.filter(mobile_no=mobile_no).first()
        if check_company_hr:
            messages.error(request, 'Mobile number Already exists..!')
            return HttpResponseRedirect('/adminPanel/create/companyHR/')
        else:
            # try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                user_type=2,
                create_type=1
            )
                        
            random_number = str(random.randint(000000,999999))
            random_user_id = (first_name+random_number)
            unique_email_id = (random_user_id+"@hellohr")
            user.staffs.mobile_no=mobile_no
            user.staffs.otp=otp
            user.save()

            # send_otp(mobile_no, otp)
            request.session['mobile_no'] = mobile_no
            return HttpResponseRedirect("/register/staff/otp/")
            # except:
            #     messages.error(request, "Fail Registration")
            #     return HttpResponseRedirect("/register/staff/")
    return render(request, 'admin-panel/authentication/register-staff-page.html')



# Function to update page CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_company_hr(request):
    return render(request, 'admin-panel/update-companyhr.html')


# Function to save update CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_update_company_hr(request):
    pass


# Function to soft delete CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def soft_delete_company_hr(request):
    pass


# Function to create page Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_staff(request):
    return render(request, 'admin-panel/create-staff.html')


# Function to save Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_staff(request):
    pass


# Function to update page Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_staff(request):
    return render(request, 'admin-panel/update-staff.html')


# Function to save update Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_update_staff(request):
    pass


# Function to soft delete Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def soft_delete_staff(request):
    pass


# Function to create page Freelancer account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_freelancer(request):
    return render(request, 'admin-panel/create-freelancer.html')


# Function to save Freelancer account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_freelancer(request):
    pass


# Function to update page Freelancer account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_freelancer(request):
    return render(request, 'admin-panel/update-freelancer.html')


# Function to save update Freelancer account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_update_freelancer(request):
    pass


# Function to soft delete Freelancer account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def soft_delete_freelancer(request):
    pass