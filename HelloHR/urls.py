from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adminPanel import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('adminPanel/', include('adminPanel.urls')),
    path('', include('webpages.urls')),
    path('doLogin', views.doLogin, name='user-login'),
    path('get_user_detail/', views.GetUserDetail),
    path('user_logout/', views.user_logout, name='user-logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)