from django.urls import path
from reg_app import views

urlpatterns = [
    path('', views.users, name="signup_page"),
    path('home/', views.home_page, name="home_page"),
    path('login/', views.login_view, name='login'),
    
]
