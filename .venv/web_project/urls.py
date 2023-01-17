"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from sample_app.views import purchase_view, flower_details
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', purchase_view, name='home'),
    # path('signup/', user_views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    # path('logout/', user_views.logout_user, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    
    path('home/', purchase_view, name='purchase_home'),
    path('details/<int:my_id>/', flower_details, name='flower_details'),
    # path('adminlogin/', include('admin_login.urls')),
    path('adminview', include('admin_view.urls')),
    path('superadmin/', admin.site.urls),

    # USER PROFILE
    # path('profile/edit/', user_views.profile, name='profile-edit'),
    # path('profile/edit/pw', user_views.change_pw_view, name='profile-edit-pw'),
    # path('profile/', user_views.view_profile, name='profile'),
]

# append static root and static url to the url configuration
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)