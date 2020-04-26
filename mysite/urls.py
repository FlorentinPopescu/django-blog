"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from blogging.views import SignupPageView
# -----------------------------------
 
urlpatterns = [
    # 'admin/' changed to 'fadmin/' to improve admin security
    path('fadmin/', admin.site.urls),
    
    # user management
    path('accounts/', include('allauth.urls')),
    
    # local apps
    path('', include('blogging.urls')),
    
    # signup
    path('signup/', SignupPageView.as_view(), name="signup"),
        
    # login & logout
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    
    # password management    
    path('password_change/',
         PasswordChangeView.as_view(template_name='password_change_form.html'),
         name="password_change"),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name="password_change_done"),
    ]
