from django.urls import path
from . import views, adminViews

urlpatterns = [
    # --------------- FRONTEND -------------- |
	# path to dashboard page.
	path('dashboard/',views.dashboard, name='dashboard'),
    # path to login page.
	path('login/',views.login_page, name='login'),
    # path to create CompanyHR account page.
    path('create/companyHR/',adminViews.add_company_hr, name='add-company-hr'),
    # path to update CompanyHR account page.
    path('update/companyHR/', adminViews.update_company_hr, name='update-company-hr'),
    # path to create Staff account page.
    path('create/staff/',adminViews.add_staff, name='add-staff'),
    # path to update Staff account page.
    path('update/staff/', adminViews.update_staff, name='update-staff'),
    # path to create Freelancer account page.
    path('create/freelancer/',adminViews.add_freelancer, name='add-freelancer'),
    # path to update Freelancer account page.
    path('update/freelancer/', adminViews.update_freelancer, name='update-freelancer'),
    # --------------- BACKEND --------------- |
    # path to save CompanyHR account.
    path('save/companyHR/', adminViews.update_company_hr, name='save-company-hr'),
    # path to save update CompanyHR account.
    path('save/update/companyHR/', adminViews.update_company_hr, name='save-update-company-hr'),
    # path to delete CompanyHR account.
    path('delete/companyHR/', adminViews.update_company_hr, name='delete-company-hr'),
    # path to save Staff account.
    path('save/staff/', adminViews.save_staff, name='save-staff'),
    # path to save update Staff account.
    path('save/update/staff/', adminViews.save_update_staff, name='save-update-staff'),
    # path to delete Staff account.
    path('delete/staff/', adminViews.soft_delete_staff, name='delete-staff'),
    # path to save Freelancer account.
    path('save/freelancer/', adminViews.save_freelancer, name='save-freelancer'),
    # path to save update Freelancer account.
    path('save/update/freelancer/', adminViews.save_update_freelancer, name='save-update-freelancer'),
    # path to delete Freelancer account.
    path('delete/freelancer/', adminViews.soft_delete_freelancer, name='delete-freelancer'),
    
]