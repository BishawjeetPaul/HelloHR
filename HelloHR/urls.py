from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adminPanel import views


urlpatterns = [
    # path to admin page.
    path("admin/", admin.site.urls),
    # --------------- FRONTEND -------------- |
    # path to webpages.
    path('', include('webpages.urls')),
    # path to adminPanel.
    path('hellohr/', include('adminPanel.urls')),
    # path to user login.
    path('doLogin/', views.doLogin, name='user-login'),
    # path to developer check user.
    path('get_user_detail/', views.GetUserDetail),
    # path to user logout. 
    path('user_logout/', views.user_logout, name='user-logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)