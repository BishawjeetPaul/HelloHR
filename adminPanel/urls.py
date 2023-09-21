from django.urls import path
from . import freelancerViews, views, adminViews, hrViews, staffViews, freelancerViews


app_name = 'adminPanel'

urlpatterns = [
    # =============ADMIN-URL-PATH============ |
    # ---------------------------- FRONTEND -------------------------------- |
	# path to dashboard page.
	path('admin/dashboard',adminViews.dashboard, name='admin-dashboard'),
    # path to login page.
	path('login/',views.login_page, name='login'),
    # path to create CompanyHR account page.
    path('admin/create/companyHR',adminViews.add_company_hr, name='add-company-hr'),
    # path to manage CompanyHR account page.
    path('admin/manage/companyHR', adminViews.manage_company_hr, name='manage-compay-hr'),
    # path to update CompanyHR account page.
    path('admin/update/companyHR/<str:hr_id>', adminViews.update_company_hr, name='update-company-hr'),
    # path to create Staff account page.
    path('admin/create/staff',adminViews.add_staff, name='add-staff'),
    # path to manage Staff account page.
    path('admin/manage/staff', adminViews.manage_staff, name='manage-staff'),
    # path to update Staff account page.
    path('admin/update/staff/<str:staff_id>', adminViews.update_staff, name='update-staff'),
    # path to create Freelancer account page.
    path('admin/create/freelancer',adminViews.add_freelancer, name='add-freelancer'),
    # path to manage Freelancer account page.
    path('admin/manage/freelance', adminViews.manage_freelancer, name='manage-freelancer'),
    # path to update Freelancer account page.
    path('admin/update/freelancer/<str:freelancer_id>', adminViews.update_freelancer, name='update-freelancer'),
    # ---------------------------- BACKEND -------------------------------- |
    # path to save CompanyHR account.
    path('admin/save/companyHR', adminViews.save_company_hr, name='save-company-hr'),
    # path to save update CompanyHR account.
    path('admin/save/update/companyHR', adminViews.save_update_company_hr, name='save-update-company-hr'),
    # path to delete CompanyHR account.
    path('admin/delete/companyHR/<str:hr_id>', adminViews.soft_delete_company_hr, name='delete-company-hr'),
    # path to save Staff account.
    path('admin/save/staff', adminViews.save_staff, name='save-staff'),
    # path to save update Staff account.
    path('admin/save/update/staff', adminViews.save_update_staff, name='save-update-staff'),
    # path to delete Staff account.
    path('admin/delete/staff/<str:staff_id>', adminViews.soft_delete_staff, name='delete-staff'),
    # path to save Freelancer account.
    path('admin/save/freelancer', adminViews.save_freelancer, name='save-freelancer'),
    # path to save update Freelancer account.
    path('admin/save/update/freelancer', adminViews.save_update_freelancer, name='save-update-freelancer'),
    # path to delete Freelancer account.
    path('admin/delete/freelancer/<str:freelancer_id>', adminViews.soft_delete_freelancer, name='delete-freelancer'),

    # =============HR-URL-PATH============ |
    # ---------------------------- FRONTEND ------------------------------- |
    # path to dashboard page.
	path('hr/dashboard',hrViews.dashboard, name='hr-dashboard'),
    path('hr/candidate/detail',hrViews.candidate_detail, name='hr-candidate-detail'),
    path('hr/candidate/manage',hrViews.candidate_manage, name='hr-candidate-manage'),
    # ---------------------------- BACKEND -------------------------------- |


    # =============STAFF-URL-PATH============ |
    # ---------------------------- FRONTEND ------------------------------- |
    # path to dashboard page.
	path('staff/dashboard',staffViews.dashboard, name='staff-dashboard'),
	path('staff/candidate/submission',staffViews.candidate_submission, name='staff-candidate-submission'),


    # ---------------------------- BACKEND -------------------------------- |

    # =============FREELANCER-URL-PATH============ |
    # ---------------------------- FRONTEND ------------------------------- |
    # path to dashboard page.
	path('freelancer/dashboard',freelancerViews.dashboard, name='freelancer-dashboard'),
	path('freelancer/candidate/submission',freelancerViews.candidate_submission, name='freelancer-candidate-submission'),


    # ---------------------------- BACKEND -------------------------------- |

]