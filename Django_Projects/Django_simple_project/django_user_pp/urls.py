from django.urls import path
from django_user_pp import views

urlpatterns = [
    path('register/', views.reg_index, name='reg_index'),  # Sign Up path
    path('login/', views.user_login, name='user_login'),   # Login path
    path('logout/', views.user_logout, name='user_logout') # Logout path
]
