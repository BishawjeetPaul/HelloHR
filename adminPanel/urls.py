from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/',views.dashboard, name='dashboard'),
	path('login/',views.login_page, name='login'),
    # path('create/user',views.create_user, name='create_user'),
]