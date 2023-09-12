from django.shortcuts import render #Used to render the .html pages.
from . models import CustomUser, CompanyHR, Staffs,Freelancer # From models.py.
from django.contrib import messages # Return messages.
from django.http import HttpResponseRedirect # Redirect the pages.
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Destroy the section after logout.
import random # Generated random numbers.




# Function to create page CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_company_hr(request):
    return render(request, 'admin-panel/companyHR/create-companyhr.html')


# Function to save CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_company_hr(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        birth_date = request.POST.get('birth_date')

        random_number = str(random.randint(000000,999999))
        l_first_name = first_name.lower()
        random_user_id = (l_first_name+random_number)
        unique_email_id = (random_user_id+"@hellohr")
        print(unique_email_id)

        check_company_hr = CompanyHR.objects.filter(mobile_no=mobile_no).first()
        if check_company_hr:
            messages.error(request, 'Mobile number Already exists..!')
            return HttpResponseRedirect('/adminPanel/create/companyHR/')

        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=unique_email_id,
                username=username,
                password=password,
                user_type=2,
                create_type=1
            )

            user.companyhr.hr_email=email
            user.companyhr.mobile_no=mobile_no
            user.companyhr.password=password
            user.companyhr.address=address
            user.companyhr.gender=gender
            user.companyhr.birth_date=birth_date
            user.save()
            messages.success(request, 'Successfully Added HR')
            return HttpResponseRedirect('/adminPanel/create/companyHR/')
        except:
            messages.error(request, "Failed to Added HR")
            return HttpResponseRedirect("/adminPanel/create/companyHR/")


# Function to manage CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def manage_company_hr(request):
    company_hr = CompanyHR.objects.all()
    context = {
        'companyhrs': company_hr,
    }
    return render(request, 'admin-panel/companyHR/manage-companyhr.html', context)


# Function to update page CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_company_hr(request, hr_id):
    company_hr = CompanyHR.objects.get(admin=hr_id)
    context = {
        'company_hr': company_hr,
        'id': hr_id,
    }
    return render(request, 'admin-panel/companyHR/update-companyhr.html', context)


# Function to save update CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_update_company_hr(request):
    if request.method == 'POST':
        hr_id = request.POST.get('hr_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        birth_date = request.POST.get('birth_date')

        try:
            user = CustomUser.objects.get(id=hr_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.password = password
            user.save()

            company_hr_model = CompanyHR.objects.get(admin=hr_id)
            company_hr_model.hr_email=email
            company_hr_model.mobile_no=mobile_no
            company_hr_model.password=password
            company_hr_model.address=address
            company_hr_model.gender=gender
            company_hr_model.birth_date=birth_date
            company_hr_model.save()
            messages.success(request, 'Successfully updated HR')
            return HttpResponseRedirect('/adminPanel/update/companyHR/'+hr_id)
        except:
            messages.error(request, "Failed to updated HR")
            return HttpResponseRedirect("/adminPanel/update/companyHR/"+hr_id)


# Function to soft delete CompanyHR account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def soft_delete_company_hr(request, hr_id):
    company_hr = CompanyHR.objects.get(admin=hr_id)
    company_hr.isDelete=True
    company_hr.save()
    messages.success(request, 'HR Deleted Successfully')
    return HttpResponseRedirect('/adminPanel/manage/companyHR/')


# Function to create page Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_staff(request):
    return render(request, 'admin-panel/create-staff.html')


# Function to save Staff account.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_staff(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        birth_date = request.POST.get('birth_date')

        random_number = str(random.randint(000000,999999))
        l_first_name = first_name.lower()
        random_user_id = (l_first_name+random_number)
        unique_email_id = (random_user_id+"@hellohr")
        print(unique_email_id)

        check_staff = Staffs.objects.filter(mobile_no=mobile_no).first()
        if check_staff:
            messages.error(request, 'Mobile number Already exists..!')
            return HttpResponseRedirect('/adminPanel/create/staff/')

        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=unique_email_id,
                username=username,
                password=password,
                user_type=3,
                create_type=1
            )

            user.staff.hr_email=email
            user.staff.mobile_no=mobile_no
            user.staff.password=password
            user.staff.address=address
            user.staff.gender=gender
            user.staff.birth_date=birth_date
            user.save()
            messages.success(request, 'Successfully Added Staff')
            return HttpResponseRedirect('/adminPanel/create/staff/')
        except:
            messages.error(request, "Failed to Added Staff")
            return HttpResponseRedirect("/adminPanel/create/staff/")
            


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
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        birth_date = request.POST.get('birth_date')

        random_number = str(random.randint(000000,999999))
        l_first_name = first_name.lower()
        random_user_id = (l_first_name+random_number)
        unique_email_id = (random_user_id+"@hellohr")
        print(unique_email_id)

        check_freelancer = Freelancer.objects.filter(mobile_no=mobile_no).first()
        if check_freelancer:
            messages.error(request, 'Mobile number Already exists..!')
            return HttpResponseRedirect('/adminPanel/create/freelancer/')

        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=unique_email_id,
                username=username,
                password=password,
                user_type=4,
                create_type=1
            )

            user.freelancer.hr_email=email
            user.freelancer.mobile_no=mobile_no
            user.freelancer.password=password
            user.freelancer.address=address
            user.freelancer.gender=gender
            user.freelancer.birth_date=birth_date
            user.save()
            messages.success(request, 'Successfully Added HR')
            return HttpResponseRedirect('/adminPanel/create/freelancer/')
        except:
            messages.error(request, "Failed to Added HR")
            return HttpResponseRedirect("/adminPanel/create/freelancer/")
            


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