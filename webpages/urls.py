from django.urls import path
from . import views

app_name="webpages"

urlpatterns = [
	path('',views.home, name='home'),
	path('contact',views.contact, name='contact'),
	path('aboutus',views.aboutus, name='aboutus'),
	path('service',views.service, name='service'),
	path('gellary',views.gellary, name='gellary'),

]