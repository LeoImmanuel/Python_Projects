"""Sample_Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("",include('home_app.urls')), # root URL
    path("first_app/",include('first_app.urls')), 
    path("user/",include('user_app.urls')),  # user page URL
    path("reg/",include('reg_app.urls')),  # Form Sign Up page URL
    path("user_auth/", include(('django_user_pp.urls', 'django_user_pp'), namespace='django_user_pp')), # Django Form Sign Up & Login page URL
    path("admin/", admin.site.urls),
]

